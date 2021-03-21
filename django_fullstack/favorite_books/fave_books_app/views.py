from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from login_app.models import User
# Create your views here.
def index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        context = {
            'books': Book.objects.all(),
            'this_user': User.objects.get(id = request.session['user_id'])
        }
        return render(request, 'books_index.html', context)

def add_book(request):
    if request.method == 'POST':
        message_errors = Book.objects.validator(request.POST)
        if len(message_errors) > 0:
            for key, value in message_errors.items():
                messages.error(request, value)
        else:
            user = User.objects.get(id = request.session['user_id'])
            book = Book.objects.create(
                title = request.POST['title'],
                desc = request.POST['desc'],
                creator = user
            )
            user.user_favorites.add(book)
    return redirect('/books')

def show_book(request, book_id):
    context = {
        'book': Book.objects.get(id = book_id),
        'current_user': User.objects.get(id = request.session['user_id'])
    }
    return render(request, "show_book.html", context)

def favorite_book(request, book_id):
    user = User.objects.get(id = request.session['user_id'])
    book = Book.objects.get(id = book_id)
    user.user_favorites.add(book)
    return redirect(f'/books/{book_id}')

def unfavorite_book(request, book_id):
    user = User.objects.get(id = request.session['user_id'])
    book = Book.objects.get(id=book_id)
    user.user_favorites.remove(book)
    return redirect(f'/books/{book_id}')

def update_desc(request, book_id):
    book = Book.objects.get(id=book_id)
    book.desc = request.POST['desc']
    book.save
    return redirect(f'/books/{book_id}')

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('/books')