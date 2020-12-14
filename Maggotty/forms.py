from django import forms
from Maggotty.models import UserProfileInfo, Poll, Event, ContactUs, Feedback
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):    
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    grade_year = forms.CharField(max_length=4, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','grade_year', 'password1', 'password2', 'email')
        
        def save(self, commit=True):
            user = super().save(commit=False)
            user.email = self.cleaned_data['email']
            user.firstname = self.cleaned_data['firstname']
            user.lastname = self.cleaned_data['lastname']
            if commit:
                user.save()
                return user
        
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
