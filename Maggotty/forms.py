from django import forms
<<<<<<< HEAD
from Maggotty.models import UserProfileInfo, Poll
=======
from Maggotty.models import Event, UserProfileInfo
>>>>>>> 625c1ea148453707970a921ece247a254dc5a506
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')

class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        
    )

class CreateEventForm(forms.ModelForm):    
   
    class Meta:
        model = Event
        fields = ['eventName', 'eventDesc', 'fromDate', 'toDate','timings','ticket']        
    

