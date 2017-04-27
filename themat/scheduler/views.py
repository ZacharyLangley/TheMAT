from django.shortcuts import render, redirect, render_to_response
from .models import Venue, Event
from scheduler.models import Event, Venue, UserProfile
from scheduler.forms import EventForm, VenueForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.models import User

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
    print(venue.views)
    return response

def event_detail(request, event_id):
    rc = RequestContext(request)

    event = Event.objects.get(id=event_id)
    venue = Venue.objects.get(id=event.location.id)
    context = {'event': event, 'venue': venue}

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
    print(event.views)
    print(event)

    return response

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
                return HttpResponseRedirect('/#/')
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

        if request.method == 'POST':
            form = EventForm(request.POST)

            if form.is_valid():
                form.save(commit=True)
                return HttpResponseRedirect("/add_event/")

            else:
                print (form.errors)

        else:
            form = EventForm()
            context_dict['form'] = form
            return render_to_response('add_event.html', context_dict, context)

    else:
        return HttpResponseRedirect('/login/')  # if user is not logged in, go to log in screen



@login_required
def userprofile(request):
    context = RequestContext(request)
    context_dict = {}
    u = User.objects.get(username=request.user)
    try:
        up = UserProfile.object.get(user=u)
    except:
        up = None
    context_dict['user'] = u
    context_dict['userprofile'] = up
    return render_to_response('userprofile.html', context_dict, context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/#/')
