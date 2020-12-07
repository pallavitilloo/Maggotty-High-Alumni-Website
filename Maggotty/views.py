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
    return render(request, "Maggotty/contribute.html")

def mycart(request):
    return render(request, "Maggotty/mycart.html")

def eventinfo(request):
    return render(request, "Maggotty/eventinfo.html")

def eventdetails(request):
    return render(request, "Maggotty/eventdetails.html")

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

    