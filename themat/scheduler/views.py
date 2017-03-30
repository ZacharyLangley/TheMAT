from django.shortcuts import render, redirect
from .models import Venue

# Create your views here.
def index(request):
    venues = Venue.objects.all()
    context = {'venues': venues}
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
