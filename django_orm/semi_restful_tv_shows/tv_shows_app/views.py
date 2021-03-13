from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def index(request):
    context = {
        'shows': show.objects.all()
    }
    return render(request, "shows.html", context)

def new(request):
    return render(request, 'new.html')

def create(request):
    show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        desc = request.POST['desc']
    )
    return redirect('/shows/')

def show_page(request, show_id):
    Show = show.objects.get(id=show_id)
    context = {
        "show": Show
    }
    return render(request, "page.html", context)

def delete(request, show_id):
    Show = show.objects.get(id=show_id)
    Show.delete()
    return redirect('/shows')

def edit(request, show_id):
    Show = show.objects.get(id=show_id)
    context = {
        "show": Show
    }
    return render(request, "edit.html", context)

def update(request, show_id):
    Show = show.objects.get(id = show_id)
    Show.title = request.POST['title']
    Show.network = request.POST['network']
    Show.release_date = request.POST['release_date']
    Show.desc = request.POST['desc']
    Show.save()
    return redirect('/shows')
