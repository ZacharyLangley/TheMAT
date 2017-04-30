from django import forms
from scheduler.models import Event, Venue, UserProfile
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget

class EventForm(forms.ModelForm):
    event_title = forms.CharField(widget=forms.TextInput(attrs={'style' : 'color:black'}),max_length=128, help_text="Event Title: ")
    begin_date = forms.DateField(widget=SelectDateWidget(attrs={'style' : 'color:black'}, empty_label=("Choose Year", "Choose Month", "Choose Day"),), help_text="Begin date: ")     # adds drop down menu
    begin_time = forms.TimeField(input_formats=('%I:%M%p', '%I:%M %p'), widget=forms.TimeInput(attrs={'style' : 'color:black'}, format=('%I:%M%p')), help_text="Begin time: (Example: 12:00PM)")
    end_date = forms.DateField(widget=SelectDateWidget(attrs={'style' : 'color:black'}, empty_label=("Choose Year", "Choose Month", "Choose Day"),), help_text="End date:")
    end_time = forms.TimeField(input_formats=('%I:%M%p', '%I:%M %p'), widget=forms.TimeInput(attrs={'style' : 'color:black'}, format=('%I:%M%p')), help_text="End time: ")
    event_description = forms.CharField(widget=forms.TextInput(attrs={'style' : 'color:black'}),max_length=128, help_text="Event Description: ")
    img_url = forms.URLField(widget=forms.TextInput(attrs={'style' : 'color:black'}), help_text="Image URL: ", required=False)

    class Meta:
        model = Event
        fields = ('event_title', 'begin_date', 'begin_time', 'end_date', 'end_time', 'event_description', 'img_url')

class VenueForm(forms.ModelForm):
    Vname = forms.CharField(required=True, max_length=128,help_text="Venue: ")
    location = forms.CharField(required=True, max_length=128, help_text="Location: ")
    rating = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Venue
        fields = ('Vname', 'location', 'rating', 'views', 'likes')

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'style' : 'color:black'}), help_text="* Username: ")
    email = forms.CharField(widget=forms.TextInput(attrs={'style' : 'color:black'}), help_text="* Email: ")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'style' : 'color:black'}), help_text="* Password: ")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'style' : 'color:black'}), help_text="* Confirm Password: ", required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    def clean(self):
            cleaned_data = super(UserForm, self).clean()
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")
            if password != confirm_password:
                raise forms.ValidationError("Password and Confirmation Password do not match")


class UserProfileForm(forms.ModelForm):
    website = forms.URLField(widget=forms.TextInput(attrs={'style' : 'color:black'}), help_text="Website: ", required=False)
    picture = forms.ImageField(help_text="Image: ", required=False)

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
