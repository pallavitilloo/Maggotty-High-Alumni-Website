from django import forms
from Maggotty.models import Poll, Event, ContactUs, Feedback
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import EmailInput, PasswordInput
from django.db import models

class RegisterForm(UserCreationForm):    
    username = forms.CharField(max_length=100)    
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(widget=EmailInput)
    
    class Meta:
        model = User
        fields = ["username", "password1","password2","first_name","last_name","email"]

class CreateEventForm(forms.ModelForm):

    class Meta:
        model = Event
        widgets = {
            'fromDate': forms.DateInput(attrs={'type': 'date'}),
            'toDate': forms.DateInput(attrs={'type': 'date'}),
            'startTime': forms.TimeInput(attrs={'type': 'time'}),
            'endTime': forms.TimeInput(attrs={'type': 'time'})
        }
        fields = ['eventName', 'eventDesc', 'fromDate',
                  'toDate', 'startTime', 'endTime', 'ticket']

        def clean(self):
            eventName = self.cleaned_data.get('eventName')

            if len(eventName) < 25:
                raise forms.ValidationError(
                    _("Minimum characters required are 25."))
            return eventName

class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs        
        fields = ['name','email','subject','comments']

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback        
        fields = ['fname','lname','email','contact','feedback']
