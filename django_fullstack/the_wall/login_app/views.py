from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt
# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
        User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            birthday = request.POST['birthday'],
            email = request.POST['email'],
            password = pw_hash
        )
        messages.info(request, "User registered; log in now")
    return redirect('/')

def login(request):
    try:
        user = User.objects.get(email = request.POST['email'])
    except:
        messages.error(request, "Email address or password is incorrect")
        return redirect("/")
    if not bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        messages.error(request, "Email address or password is incorrect")
        return redirect("/")
    else:
        request.session['user_id'] = user.id
        request.session['user_first_name'] = user.first_name
        request.session['user_email'] = user.email
        messages.success(request, "You have successfully registered!")
        return redirect('/success')
    
def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id = request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, 'success.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')