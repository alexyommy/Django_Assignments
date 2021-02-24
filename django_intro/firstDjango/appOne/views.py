from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("I am ready to handle a request for '/'!")

# Create your views here.
def one_method(request):                # no values passed via URL
    pass
    
def another_method(request, my_val):	# my_val would be a number from the URL
    pass                                # given the example above, my_val would be 23
    
def yet_another(request, name):         # name would be a string from the URL
    pass                                # given the example above, name would be 'pooh'
    
def one_more(request, id, color): 	# id would be a number, and color a string from the URL
    pass                            # given the example above, id would be 17 and color would be 'brown'