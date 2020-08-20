from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def water(request):
    return HttpResponse("Drink 5ltrs of water daily to stay healthy.")
def food(request):
    return HttpResponse("Donot eat junk food")
