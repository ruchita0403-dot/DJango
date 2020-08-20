from django.contrib import admin
from django.urls import path
from contacts import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'friends.*', views.friends,name='friends'),
    url(r'family.*',views.family,name='family'),
]
