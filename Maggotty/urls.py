from django.urls import path
from Maggotty import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
admin.autodiscover()

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),    
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("donate/", views.donate, name="donate"),
    path("faq/", views.faq, name="faq"),
    path("feedback/", views.feedback, name="feedback"),
    path("history/", views.history, name="history"),
    path("mission/", views.mission, name="mission"),
    path("news/", views.news, name="news"),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name='Maggotty/login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name='Maggotty/logout.html'), name="logout"),
    path("admin/", admin.site.urls),    
    path("contribute/", views.contribute, name="contribute"),
    path("contributions/", views.contributions, name='contributions'),
    path("polls", views.polls, name="polls"),
    path("approved_polls", views.approvedPolls, name="approved_polls"),
    path("mycart/", views.mycart, name="mycart"),
    path("eventinfo/", views.eventinfo, name="eventinfo"),
    path("eventdetails/", views.eventdetails, name="eventdetails"),
    path("newsdetail/", views.newsdetail, name="newsdetail")
]