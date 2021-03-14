from django.shortcuts import redirect, render
from django.contrib import messages

from .models import *
from datetime import datetime


# Create your views here.
def index(request):
    context = {
        'shows': show.objects.all()
    }
    return render(request, "shows.html", context)

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method =='POST':
        errors = show.objects.validate(request.POST)
        if errors:
            for (key, value) in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        else:
            newShow = show.objects.create(
                title = request.POST['title'],
                network = request.POST['network'],
                release_date = request.POST['release_date'],
                desc = request.POST['desc']
            )
            newShow.save()
            return redirect(f'/shows/{newShow.id}')
    return redirect("/")

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
    errors = show.objects.validate(request.POST)
    if errors:
        for (key, value) in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show_id}/edit')
    Show = show.objects.get(id = show_id)
    Show.title = request.POST['title']
    Show.network = request.POST['network']
    Show.release_date = request.POST['release_date']
    Show.desc = request.POST['desc']
    Show.save()
    return redirect(f'/shows/{show_id}')
