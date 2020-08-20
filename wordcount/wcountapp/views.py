from django.shortcuts import render
import operator
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'wcountapp/home.html')

def count(request):
    recvtxt=request.GET['fulltext']
    wcount=recvtxt.split()
    mydict={}
    for i in wcount:
        if i in mydict:
            mydict[i]+=1
        else:
            mydict[i]=1
    return render(request,'wcountapp/count.html',{'mycount':wcount,'yourdict':mydict})