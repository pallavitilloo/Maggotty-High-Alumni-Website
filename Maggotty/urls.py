from django.urls import path
from Maggotty import views

urlpatterns = [
    path("", views.home, name="home"),
    path("Maggotty/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("donate/", views.donate, name="donate"),
    path("faq/", views.faq, name="faq"),
    path("feedback/", views.feedback, name="feedback"),
    path("history/", views.history, name="history"),
    path("mission/", views.mission, name="mission"),
    path("news/", views.news, name="news"),
]