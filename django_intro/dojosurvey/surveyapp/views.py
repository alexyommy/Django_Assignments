from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if "prev_name" not in request.session:
        request.session['prev_name'] = "no one"
    return render(request, "index.html")

def result(request):
    if request.method == 'GET':
        return redirect('/')
    context = {
        "name": request.POST["name"],
        "occupation": request.POST["occupation"],
        "locations": request.POST["locations"],
        "languages": request.POST["languages"],
        "comments": request.POST["comments"],
        "prev_name": request.session["prev_name"],
    }
    request.session["prev_name"] = request.POST["name"]
    return render(request, "result.html", context)



