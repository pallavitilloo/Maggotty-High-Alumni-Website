import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from Maggotty.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Maggotty.models import Event
from django.db import models

from Maggotty.models import Contribute, Poll, UserOpinions

def home(request):
    return render(request, "Maggotty/home.html")

def about(request):
    return render(request, "Maggotty/about.html")

def contact(request):
    return render(request, "Maggotty/contact.html")

def donate(request):
    return render(request, "Maggotty/donate.html")

def faq(request):
    return render(request, "Maggotty/faq.html")

def feedback(request):
    return render(request, "Maggotty/feedback.html")

def history(request):
    return render(request, "Maggotty/history.html")

def mission(request):
    return render(request, "Maggotty/mission.html")

def news(request):
    return render(request, "Maggotty/news.html")

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            messages.success(request, f'{user}')
            return redirect('home')
            return redirect('login')
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'Maggotty/register.html',
                  {'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})

def event(request):
    return render(request, "Maggotty/event.html")

def eventlist(request):
    return render(request, "Maggotty/eventlist.html")

def contribute(request):
    """Handle Content Upload"""
    if request.method == 'POST':
        contribute_title = request.POST['title']
        contribute_img = request.FILES['filename']
        contribute_description = request.POST['comment']

        # create  and save an instance of the Contribute model
        contribution = Contribute(title=contribute_title, upload=contribute_img, description=contribute_description)
        contribution.save()

    return render(request, "Maggotty/contribute.html")


def contributions(request):
    contributions = Contribute.objects.all()[:3]
    return render(request, "Maggotty/contributions.html", {"contributions": contributions})


def polls(request):
    # retrieve all the poll questions from the database
    polls = Poll.objects.all()

    if request.method == 'POST':
        answer_1 = request.POST['1']
        answer_2 = request.POST['2']
        answer_3 = request.POST['opinion']
        question_1 = polls[0].question
        question_2 = polls[1].question
        user_poll = UserOpinions(question_1=question_1, question_2=question_2, answers_1=answer_1, answers_2=answer_2, username=request.user, opinion=answer_3)
        user_poll.save()
    
    return render(request, "Maggotty/polls.html", {"polls": polls})


def approvedPolls(request):
    polls = UserOpinions.objects.filter(approved=True)
    return render(request, "Maggotty/allpolls.html", {"polls": polls})


def mycart(request):
    return render(request, "Maggotty/mycart.html")

def eventinfo(request):
    return render(request, "Maggotty/eventinfo.html")

def eventdetails(request):
    return render(request, "Maggotty/eventdetails.html")

def newsdetail(request):
    return render(request, "Maggotty/newsdetail.html")


def hello_there(request, name):
    
    return render(
        request,
        'Maggotty/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

# def event(request):    
#     if request.method == 'POST':
#         if request.POST.get('title') and request.POST.get('content'):
#             post=Event()            
#             post.title= request.POST.get('title')
#             post.content= request.POST.get('content')
#             post.save()            
#             return render(request, 'Maggotty/event.html')  

#     else:
#         return render(request,'Maggotty/event.html')

    