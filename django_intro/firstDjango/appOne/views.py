from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, "index.html")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse(f"placeholder to display a blog number: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request, number):
    return redirect("/")

def hello_name(request, name):
    context = {
        "htmlname": name,
        "namelist": ["Alex", "Albert", "Ryan"]
    }
    return render(request, "helloname.html", context)

# Create your views here.
def one_method(request):                # no values passed via URL
    pass
    
def another_method(request, my_val):	# my_val would be a number from the URL
    pass                                # given the example above, my_val would be 23
    
def yet_another(request, name):         # name would be a string from the URL
    pass                                # given the example above, name would be 'pooh'
    
def one_more(request, id, color): 	# id would be a number, and color a string from the URL
    pass                            # given the example above, id would be 17 and color would be 'brown'
