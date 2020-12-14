from django import forms
from Maggotty.models import UserProfileInfo, Poll, Event
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
        widgets = {
            'fromDate': forms.DateInput(attrs={'type':'date'}),
            'toDate' : forms.DateInput(attrs={'type':'date'})
        }
        fields = ['eventName', 'eventDesc', 'fromDate', 'toDate','timings','ticket']        
    

