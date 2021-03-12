from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def index(request):
    return render(request, "index.html")

def show_books(request):
    return render(request, "books.html", {"books": book.objects.all()})

def show_authors(request):
    return render(request, "authors.html", {"authors": author.objects.all()})


def add_book(request):
    book.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc']
    )
    return redirect('/books')

def add_author(request):
    author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes']
    )
    return redirect('/authors')

def show_book(request, book_id):
    Book = book.objects.get(id=book_id)
    context = {
        "book": Book,
        "authors": author.objects.exclude(books__id=book_id)
    }
    return render(request, "book.html", context)

def show_author(request, author_id):
    Author = author.objects.get(id=author_id)
    context = {
        "author": Author,
        "books": book.objects.exclude(authors__id=author_id)
    }
    return render(request, "author.html", context)

def assign_book(request, book_id):
    Book = book.objects.get(id=book_id)
    Author = author.objects.get(id=request.POST['author_id'])
    Book.authors.add(Author)
    return redirect(f'/book/{book_id}')

def assign_author(request, author_id):
    Author = author.objects.get(id=author_id)
    Book = book.objects.get(id=request.POST['book_id'])
    Author.books.add(Book)
    return redirect(f'/author/{author_id}')



