from django.contrib.messages.api import error
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
        'courses': course.objects.all()
    }
    return render(request, "course.html", context)

def add(request):
    if request.method == 'POST':
        errors = course.objects.validate(request.POST)
        if errors:
            for (key, value) in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            newCourse = course.objects.create(
                course_name = request.POST['course_name'],
                description = request.POST['description']
            )
            newCourse.save()
    return redirect("/")

def destroy(request, course_id):
    Course = course.objects.get(id=course_id)
    context = {
        "course": Course
    }
    return render(request, "destroy.html", context)

def delete(request, course_id):
    Course = course.objects.get(id=course_id)
    Course.delete()
    return redirect('/')

