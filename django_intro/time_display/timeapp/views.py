from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

# Create your views here.
def index(request):
    return HttpResponse("You about to find out the time!")

def time(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'time.html',context)

