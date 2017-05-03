from django.shortcuts import render, redirect, render_to_response
from .models import Venue, Event
from scheduler.models import Event, Venue, UserProfile, AttendEvent
from scheduler.forms import EventForm, VenueForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView, CreateView, DeleteView

# Create your views here.
def index(request):
    rc = RequestContext(request)

    venues = Venue.objects.all()
    events = Event.objects.all()
    context = {'venues': venues, 'events': events}

    response = render_to_response('index.html', context, rc)
    #visits = int(request.COOKIES.get('visits', '0'))

    #if 'last_visit' in request.COOKIES:
        #print("cookie exists")
        #last_visit = request.COOKIES['last_visit']
        #last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

        #if (datetime.now() - last_visit_time).days > 0:
            #response.set_cookie("visits", visits+1)
            #response.set_cookie('last_visit', datetime.now())
    #else:
        #print("Cookies don exits")
        #response.set_cookie('last_visit', datetime.now())

    return response

def venue_list(request):
    venues = Venue.objects.all()
    context = {'venues': venues}
    return render(request, 'venue_list.html', context)

def venue_detail(request, venue_id):
    rc = RequestContext(request)

    venue = Venue.objects.get(id=venue_id)
    events = Event.objects.filter(location=venue)
    if request.user.is_authenticated():  # make sure user is logged in
        up = UserProfile.objects.get(user=request.user)
        context = {'venue': venue, 'events': events, 'up':up}
    else:
        context = {'venue': venue, 'events': events}

    response = render_to_response('venue_detail.html', context, rc)

    if 'last_visitV'+str(venue_id) in request.COOKIES: #cookie exists
        last_visit = request.COOKIES['last_visitV'+str(venue_id)]
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

        if (datetime.now() - last_visit_time).days > 0:
            venue.views += 1
            venue.save()
            response.set_cookie('last_visitV'+str(venue_id), datetime.now())
    else: #cookie don exits
        response.set_cookie('last_visitV'+str(venue_id), datetime.now())
        venue.views += 1
        venue.save()
    return response

def event_detail(request, event_id):
    rc = RequestContext(request)

    # Retrieve event page inforamtion
    event = Event.objects.get(id=event_id)
    venue = Venue.objects.get(id=event.location.id)
    attendance = AttendEvent.objects.filter(event=event.id)
    attendanceprofiles = []
    for a in attendance:
        profile = UserProfile.objects.get(user=a.user)
        pair = (a.user, profile)
        attendanceprofiles.append(pair)
    if request.user.is_authenticated():  # make sure user is logged in
        # Check if the user is marked as attending this event
        try:
            userattendeance = AttendEvent.objects.get(user=request.user, event=event_id)
        except:
            userattendeance = False
        # Retrieve current user's profile to see if they are the
        # event's venue manager
        up = UserProfile.objects.get(user=request.user)
        context = {'venue': venue, 'event': event,
                    'attendance': attendance,'up':up,
                    'userattendeance': userattendeance,
                    'attendanceprofiles':attendanceprofiles}
    else:
        context = {'venue': venue, 'event': event, 'attendance':attendance,
        'attendanceprofiles':attendanceprofiles}

    response = render_to_response('event_detail.html', context, rc)

    if 'last_visitE'+str(event_id) in request.COOKIES: #cookie exists
        last_visit = request.COOKIES['last_visitE'+str(event_id)]
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

        if (datetime.now() - last_visit_time).days > 0:
            event.views += 1
            event.save()
            response.set_cookie('last_visitE'+str(event_id), datetime.now())
    else: #cookie don exits
        response.set_cookie('last_visitE'+str(event_id), datetime.now())
        event.views += 1
        event.save()

    return response

def attend_event(request, event_id):
    if request.user.is_authenticated():
        user = User.objects.get(id=request.user.id)
        event = Event.objects.get(id=event_id)
        try:
            checkattendance = AttendEvent.objects.get(user=user, event=event)
        except:
            checkattendance = False

        # If the user is not already attending, mark them as attending
        if checkattendance is False:
            attendance = AttendEvent(user=user, event=event)
            attendance.save()
            return redirect(event.get_absolute_url())
        # Else, send them back to the event page
        else:
            return redirect(event.get_absolute_url())
    else:
        return redirect('/login')

def unattend_event(request, event_id):
    if request.user.is_authenticated():
        user = User.objects.get(id=request.user.id)
        event = Event.objects.get(id=event_id)
        try:
            attendance = AttendEvent.objects.get(user=user, event=event)
        except:
            attendance = False

        if attendance is not False:
            attendance.delete()
        else:
            return redirect(event.get_absolute_url())

        return redirect(event.get_absolute_url())
    else:
        return redirect('/login')

def user_login(request):
    context = RequestContext(request)
    context_dict = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                context_dict['disabled_account'] = True
                return HttpResponse("Your MAT account is disabled.")
        else:
            #print "Invalid login details: {0}, {1}".format(username, password)
            context_dict['bad details'] = True
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('login.html', context_dict, context)

def register(request):
    context = RequestContext(request)
    context_dict = {}
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            pass
            #print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context_dict['user_form'] = user_form
    context_dict['profile_form']= profile_form
    context_dict['registered'] = registered

    return render_to_response(
            'register.html',
            context_dict,
            context)


def add_event(request):
    context = RequestContext(request)
    context_dict = {}
    if request.user.is_authenticated():  # make sure user is logged in
        venue_manager = UserProfile.objects.get(user=request.user)
        if venue_manager.is_venue:  # make sure manages a venue
            if request.method == 'POST':
                form = EventForm(request.POST)
                if form.is_valid():
                    venue_manager = UserProfile.objects.get(user=request.user)
                    event = form.save(commit=False)
                    event.location = venue_manager.location
                    event.begin_date = str(form.cleaned_data['begin_date']) + ' ' + str(form.cleaned_data['begin_time'])
                    event.end_date = str(form.cleaned_data['end_date']) + ' ' + str(form.cleaned_data['end_time'])
                    event.save()
                    url = '/event/' +  str(event.id)
                    return redirect(url)
                else:
                    print (form.errors)
            else:
                form = EventForm()
                context_dict['form'] = form
                return render_to_response('add_event.html', context_dict, context)
        else:
            return redirect('/')

    else:
        return HttpResponseRedirect('/login/')  # if user is not logged in, go to log in screen

class UpdateEvent(UpdateView):
    model = Event
    form_class = EventForm

    #Checks to see if user is logged in and is updating their own object
    def user_passes_test(self, request):
        if request.user.is_authenticated():
            venue_manager = UserProfile.objects.get(user=request.user)
            self.object = self.get_object()
            return self.object.location == venue_manager.location
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect('/')
        return super(UpdateEvent, self).dispatch(
            request, *args, **kwargs)

    def form_valid(self, form):
        # Check if category matches subcategory
        self.object.begin_date = str(form.cleaned_data['begin_date']) + ' ' + str(form.cleaned_data['begin_time'])
        self.object.end_date = str(form.cleaned_data['end_date']) + ' ' + str(form.cleaned_data['end_time'])
        return super(UpdateEvent, self).form_valid(form)


class DeleteEvent(DeleteView):
    model = Event
    success_url = '/'
    login_url = '/login/'

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        if self.request.user.is_authenticated():
            obj = super(DeleteEvent, self).get_object()
            venue_manager = UserProfile.objects.get(user=self.request.user)
            if not obj.location == venue_manager.location:
                raise Http404
            return obj
        else:
            raise Http404

class UpdateVenue(UpdateView):
    model = Venue
    form_class = VenueForm

    #Checks to see if user is logged in and is updating their own object
    def user_passes_test(self, request):
        if request.user.is_authenticated():
            venue_manager = UserProfile.objects.get(user=request.user)
            self.object = self.get_object()
            return self.object == venue_manager.location
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect('/')
        return super(UpdateVenue, self).dispatch(
            request, *args, **kwargs)

    def form_valid(self, form):
        # Check if category matches subcategory
        return super(UpdateVenue, self).form_valid(form)

def userprofile(request):
    if request.user.is_authenticated():  # make sure user is logged in
        context = RequestContext(request)
        context_dict = {}
        u = User.objects.get(username=request.user)
        try:
            up = UserProfile.objects.get(user=u)
        except:
            up = None
        attendance = AttendEvent.objects.filter(user=u)
        context_dict['user'] = u
        context_dict['userprofile'] = up
        context_dict['attendance'] = attendance
        context_dict = {
            'user':u,
            'userprofile':up,
            'attendance':attendance
        }
        return render_to_response('userprofile.html', context_dict, context)
    else:
        return redirect('/login/')


def user_logout(request):
    if request.user.is_authenticated():  # make sure user is logged in
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return redirect('/login/')
