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
    eventName = models.CharField("Event Name", max_length=255, blank=False)
    eventDesc = models.TextField("Event Description", max_length=1024, blank=True, null=True)
    fromDate = models.DateField(blank=False)
    toDate = models.DateField(blank=False)
    startTime = models.TimeField()
    endTime = models.TimeField()
    ticket = models.FloatField("Ticket Price", null=True)
    isApproved = models.BooleanField("Is Approved", default=False)
    createdBy = models.CharField("Created By", max_length=255, editable=False)


    def __str__(self):
        return self.eventName

# added contribute model to store input from "upload content"/ contribute page
class Contribute(models.Model):
    title = models.CharField(max_length=255)
    upload = models.ImageField(upload_to='contribute/')
    description = models.TextField()

    def __str__(self):
        return self.title


class Poll(models.Model):
    question = models.TextField()
    choice_1 = models.CharField(max_length=34)
    choice_2 = models.CharField(max_length=34)

    def __str__(self):
        return self.question


class UserOpinions(models.Model):    
    question_1 = models.CharField(max_length=255, blank=True, null=True)
    question_2 = models.CharField(max_length=255, blank=True, null=True)
    answers_1 =  models.CharField(max_length=255, blank=True, null=True)
    answers_2 =  models.CharField(max_length=255, blank=True, null=True)
    opinion = models.TextField(default="Test Opinion")
    username = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.opinion[:10]

class Order(models.Model):
    username = models.CharField(max_length=255, blank=False)
    eventID = models.IntegerField()
    eventName = models.CharField(max_length=255)
    ticketPrice = models.FloatField()
    ifPaid = models.BooleanField(default=False)

class Feedback(models.Model):    
    fname = models.CharField(max_length=255, blank=False, verbose_name="First Name")
    lname = models.CharField(max_length=255, blank=False, verbose_name="Last Name")
    email = models.CharField(max_length=255, blank=False, verbose_name="Email")
    contact = models.CharField(max_length=255, blank=False, verbose_name="Contact Information")
    feedback = models.TextField(max_length=2000, blank=False, verbose_name="Feedback")

class ContactUs(models.Model):    
    name = models.CharField(max_length=255, blank=False, verbose_name="Name")    
    email = models.CharField(max_length=255, blank=False, verbose_name="Email")
    subject = models.CharField(max_length=255, blank=False, verbose_name="Subject")
    comments = models.TextField(max_length=2000, blank=False, verbose_name="Comments")
