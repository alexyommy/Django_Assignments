from django.shortcuts import redirect, render
from django.contrib import messages

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
    errors = show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
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
    errors = show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/edit'+id)
    else:
        Show = show.objects.get(id = show_id)
        Show.title = request.POST['title']
        Show.network = request.POST['network']
        Show.release_date = request.POST['release_date']
        Show.desc = request.POST['desc']
        Show.save()
        return redirect('/shows')

# Inside your app's views.py file
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
