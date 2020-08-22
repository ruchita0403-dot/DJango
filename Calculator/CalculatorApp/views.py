from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'CalculatorApp/home.html')

def results(request):
    a=int(request.GET["fno"])
    op=request.GET["op"]
    b=int(request.GET["sno"])
    res=0
    if(op=='+'):
        res=a+b
    elif(op=='-'):
        res=a-b
    elif(op=='*'):
        res=a*b
    elif(op=='/'):
        res=a/b
    
    return render(request,'CalculatorApp/results.html',{'a':a,'b':b,'op':op,'res':res})
