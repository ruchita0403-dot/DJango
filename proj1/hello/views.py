from django.shortcuts import render
from django.http import HttpResponse
import operator

# Create your views here.
def home(request):
    return render(request,'hello/home.html',{'name':'Ruchita'})
def hobbies(request):
    return HttpResponse("<h1>My hobbies are watching movies,listening music and reading.</h1>")
def aboutme(request):
    return render(request,'hello/about.html',{'userid':'064'})