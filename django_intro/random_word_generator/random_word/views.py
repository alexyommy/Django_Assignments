from django.shortcuts import redirect, render,

# Create your views here.
def index(request):
    return render(request, "index.html")

def result(request):
    if request.method == 'GET':
        return redirect('/')
    context = {
        
    }
    return render(request, "result.html")
