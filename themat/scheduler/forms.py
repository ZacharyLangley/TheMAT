from django import forms
from scheduler.models import Event, Venue, UserProfile
from django.contrib.auth.models import User

class EventForm(forms.ModelForm):
    title = forms.CharField(required=True, max_length=128,label="Event Title: ")
    startdate = forms.DateField(required=True, label="Start Date: ")
    enddate = forms.DateField(required=True, label="End Date: ")
    location = forms.CharField(required=True, max_length=128, label="Location: ")

    class Meta:
        model = Event
        fields = ('title', 'startdate', 'enddate', 'location')

class VenueForm(forms.ModelForm):
    Vname = forms.CharField(required=True, max_length=128,label="Venue: ")
    location = forms.CharField(required=True, max_length=128, label="Location: ")
    rating = forms.IntegerField(widget=forms.HiddenInput(), initial=50)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Venue
        fields = ('Vname', 'location', 'rating', 'views', 'likes')

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Username: ")
    email = forms.CharField(help_text="Email: ")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Password: ")
    confirm_password = forms.CharField(widget=forms.PasswordInput(),help_text="Confirm Password: ", required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean(self):
            cleaned_data = super(UserForm, self).clean()
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")
            if password != confirm_password:
                raise forms.ValidationError("Password and Confirmation Password do not match")


class UserProfileForm(forms.ModelForm):
    website = forms.URLField(help_text="Website: ", required=False)
    picture = forms.ImageField(help_text="Image: ", required=False)
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

