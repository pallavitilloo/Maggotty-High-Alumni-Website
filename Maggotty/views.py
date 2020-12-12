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

class IndexView(ListView):
    template_name = 'Maggotty/index.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        return Event.objects.all()

class EventDetailView(DetailView):
    model = Event
    template_name = 'Maggotty/eventdetails.html'

def create(request):
    if request.method == 'POST':
        form = CreateEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = CreateEventForm()

    return render(request,'Maggotty/event.html',{'form': form})

def edit(request, pk, template_name='Maggotty/edit.html'):
    event = get_object_or_404(Event, pk=pk)
    # form = CreateEventForm(request.POST or None, instance=post)
    form = CreateEventForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, template_name, {'form':form})

def delete(request, pk, template_name='Maggotty/confirm_delete.html'):
    event = get_object_or_404(Event, pk=pk)
    if request.method=='POST':
        event.delete()
        return redirect('home')
    return render(request, template_name, {'object':event})

def eventdetails(request):
    return render(request, "Maggotty/eventdetails.html")

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

    