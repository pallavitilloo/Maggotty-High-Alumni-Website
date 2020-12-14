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
            'toDate' : forms.DateInput(attrs={'type':'date'}),
            'startTime':forms.TimeInput(attrs={'type':'time'}),
            'endTime':forms.TimeInput(attrs={'type':'time'})
        }
        fields = ['eventName', 'eventDesc', 'fromDate', 'toDate','startTime','endTime','ticket']       
        def clean(self):
            eventName = self.cleaned_data.get('eventName')

            if len(eventName) < 25:
                raise forms.ValidationError(_("Minimum characters required are 25."))
            return eventName

