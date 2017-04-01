from django.shortcuts import render, redirect, render_to_response
from .models import Venue, Event
from scheduler.models import Event, Venue
from scheduler.forms import EventForm, VenueForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.template import RequestContext

# Create your views here.
def index(request):
    venues = Venue.objects.all()
    events = Event.objects.all()
    context = {'venues': venues, 'events': events}
    return render(request, 'index.html', context)

def profileList(request):
    venues = Venue.objects.all()
    context = {'venues': venues}
    return render(request, 'profileList.html', context)

def profile(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    context = {'venue': venue}
    print(venue)
    return render(request, "profile.html", context)

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


@login_required
def add_event(request):
    context = RequestContext(request)
    context_dict = {}
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = EventForm()

    context_dict['form'] = form
    return render_to_response('add_event.html', context_dict, context)



@login_required
def add_venue(request):
    return HttpResponseRedirect('/#/')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/#/')
