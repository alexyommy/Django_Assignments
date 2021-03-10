from django.shortcuts import redirect, render
from .models import book, author

# Create your views here.
def index(request):
    context = {
        'books': book.objects.all()
    }
    return render(request, "index.html", context)

def add_book(request):
    book.objects.create(
        title=request.POST['title'],
        # desc=request.POST['desc']
    )
    return redirect('/')