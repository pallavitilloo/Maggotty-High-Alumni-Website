import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from Maggotty.forms import UserForm, UserProfileInfoForm, CreateEventForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Maggotty.models import Event
from django.db import models
from django.views.generic import ListView, DetailView

# class IndexView(ListView):
#     template_name = 'Maggotty/index.html'
#     context_object_name = 'event_list'

#     def get_queryset(self):
#         return Event.objects.all()

# class EventDetailView(DetailView):
#     model = Event
#     template_name = 'Maggotty/eventdetails.html'

# def edit(request, pk, template_name='Maggotty/edit.html'):
#     event = get_object_or_404(Event, pk=pk)
#     # form = CreateEventForm(request.POST or None, instance=post)
#     form = CreateEventForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('home')
#     return render(request, template_name, {'form':form})

# def delete(request, pk, template_name='Maggotty/confirm_delete.html'):
#     event = get_object_or_404(Event, pk=pk)
#     if request.method=='POST':
#         event.delete()
#         return redirect('home')
#     return render(request, template_name, {'object':event})



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
            messages.success(request, f'✔️ User account created successfully for {user}. You can login and access your account now!')
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

def contribute(request):
    return render(request, "Maggotty/contribute.html")

def mycart(request):
    return render(request, "Maggotty/mycart.html")

# def event(request):
#     return render(request, "Maggotty/event.html")

def alleventslist(request):
    return render(request, "Maggotty/alleventslist.html")

def upcomingevents(request):
    return render(request, "Maggotty/upcomingevents.html")

def createevent(request):
    if request.method == 'POST':
        form = CreateEventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'✔️ Event created')
            return redirect('home')
    form = CreateEventForm()
    return render(request,'Maggotty/createevent.html',{'form': form})

def eventdetails(request):
    return render(request, "Maggotty/eventdetails.html")

def newsdetail(request):
    return render(request, "Maggotty/newsdetail.html")
    