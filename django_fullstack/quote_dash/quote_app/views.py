from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
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
        return redirect('/quotes')

def logout(request):
    request.session.clear()
    return redirect('/')

def quotes(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        context = {
            'quotes': Quote.objects.all(),
            'this_user': User.objects.get(id = request.session['user_id'])
        }
        return render(request, 'quotes.html', context)

def create(request):
    if request.method == 'POST':
        message_errors = Quote.objects.validator(request.POST)
        if len(message_errors) > 0:
            for key, value in message_errors.items():
                messages.error(request, value)
        else:
            Quote.objects.create(
                author = request.POST['author'],
                content = request.POST['content'],
                poster = User.objects.get(id = request.session['user_id'])
            )
    return redirect('/quotes')

def add_like(request, quote_id):
    liked_quote = Quote.objects.get(id = quote_id)
    user_liking = User.objects.get(id = request.session['user_id'])
    liked_quote.user_likes.add(user_liking)
    return redirect('/quotes')

def delete(request, quote_id):
    if request.method == 'POST':
        quote = Quote.objects.get(id = quote_id)
        quote.delete()
    return redirect('/quotes')

def show_user(request, user_id):
    context = {
        'user': User.objects.get(id = user_id)
    }
    return render(request, 'user.html', context)

def edit_user(request, user_id):
    user_id = User.objects.get(id = request.session['user_id'] )
    context = {
        "user": user_id
    }
    return render(request, 'edit.html', context)

def update(request, user_id):
    errors = User.objects.updater(request.POST)
    if errors:
        for (key, value) in errors.items():
            messages.error(request, value)
        return redirect(f'/myaccount/{user_id}')
    user = User.objects.get(id = user_id)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    return redirect(f'/myaccount/{user_id}')
