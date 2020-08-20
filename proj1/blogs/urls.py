from django.contrib import admin
from django.urls import path
from blogs import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'food.*', views.food,name='food'),
    url(r'water.*',views.water,name='water'),
]
