from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)    


def __str__(self):
    return self.user.username

class Event(models.Model):
    eventName = models.CharField("Event Name", max_length=255, blank = False, unique=True)
    eventDesc = models.TextField("Event Description", max_length=1024, blank = True, null = True)
    fromDate = models.DateTimeField("From Date", auto_now_add=False)
    toDate = models.DateTimeField("To Date", auto_now_add=False)
    timings = models.CharField("Timings", max_length=255,  blank = False, null = True)
    ticket = models.FloatField("Ticket Price", blank = True, default=0.0, null = True)
    isApproved = models.BooleanField("Is Approved", default=False)
    createdBy = models.CharField("Created By", max_length=255)
    
    def __str__(self):
        return self.eventName