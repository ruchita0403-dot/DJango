from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def friends(request):
    return HttpResponse("These are my friends contacts.")
def family(request):
    return HttpResponse("These are my family contacts.")
