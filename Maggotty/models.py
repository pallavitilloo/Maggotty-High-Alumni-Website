from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)    


def __str__(self):
    return self.user.username

class Event(models.Model):   
    
    eventName = models.CharField("Event Name", max_length=255, blank = False, unique=True, help_text="A unique name for your event", validators=[RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])
    eventDesc = models.TextField("Event Description", max_length=1024, blank = True, null = True,  help_text="A useful description for your event")
    fromDate = models.DateTimeField("From Date", help_text="MM/DD/YYYY")  
    toDate = models.DateTimeField("To Date", help_text="MM/DD/YYYY")  
    timings = models.CharField("Event Timings", max_length=255, help_text="Timings for the event") 
    ticket = models.FloatField("Ticket Price", blank = True, null = True, help_text="The ticket price for this event")
    isApproved = models.BooleanField("Is Approved", default=False)
    createdBy = models.CharField("Created By", max_length=255)
    
    def __str__(self):        
        return self.eventName
