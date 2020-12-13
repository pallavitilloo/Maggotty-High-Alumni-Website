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
    eventName = models.CharField("Event Name", max_length=255, blank=True, help_text="Alphanumeric only")
    eventDesc = models.TextField("Event Description", max_length=1024, blank=True, null=True, help_text="Description of the event")
    fromDate = models.DateTimeField("Start Date", help_text="MM/DD/YYYY")
    toDate = models.DateTimeField("End Date", help_text="MM/DD/YYYY")
    timings = models.CharField("Event Timings", max_length=255, help_text="Timings for the event")
    ticket = models.FloatField("Ticket Price", null=True, help_text="Price for the event")
    isApproved = models.BooleanField("Is Approved", default=False)
    createdBy = models.CharField("Created By", max_length=255)

    def __str__(self):
        return self.eventName

# added contribute model to store input from "upload content"/ contribute page
class Contribute(models.Model):
    title = models.CharField(max_length=255)
    upload = models.ImageField(upload_to='contribute/')
    description = models.TextField()


class Poll(models.Model):
    question = models.TextField()
    choice_1 = models.CharField(max_length=34)
    choice_2 = models.CharField(max_length=34)
    # choices = ((choice_1, choice_1), (choice_2, choice_2))
    # options = models.CharField(choices=choices, max_length=34)


class UserOpinions(models.Model):    
    question_1 = models.CharField(max_length=255)
    question_2 = models.CharField(max_length=255)
    answers_1 =  models.CharField(max_length=255)
    answers_2 =  models.CharField(max_length=255)
    opinion = models.TextField(default="Test Opinion")
    username = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)
