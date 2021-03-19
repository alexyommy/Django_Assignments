from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Wall_Message, Comment
from login_app.models import User 
# Create your views here.
def index(request):
    context = {
        'wall_messages': Wall_Message.objects.all(),
        'comments': Comment.objects.all()
    }
    return render(request, "wall_index.html", context)

def post_message(request):
    if request.method == 'POST':
        message_errors = Wall_Message.objects.validator(request.POST)
        if len(message_errors) > 0:
            for key, value in message_errors.items():
                messages.error(request, value)
        else:
            Wall_Message.objects.create(
                message = request.POST['message'], 
                user = User.objects.get(id = request.session['user_id'])
                )
    return redirect('/wall')

def post_comment(request, wall_message_id):
    if request.method == 'POST':
        comment_errors = Comment.objects.validator(request.POST)
        if len(comment_errors) > 0:
            for key, value in comment_errors.items():
                messages.error(request, value)
        else:
            Comment.objects.create(
                comment = request.POST['comment'], 
                user = User.objects.get(id = request.session['user_id']),
                message = Wall_Message.objects.get(id=wall_message_id)
                )
    return redirect('/wall')

def delete_message(request, wall_message_id):
    if request.method == 'POST':
        wall_message = Wall_Message.objects.get(id=wall_message_id)
        wall_message.delete()
    return redirect('/wall')

def delete_comment(request, comment_id):
    if request.method == 'POST':
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
    return redirect('/wall')

def show_user(request, profile_id):
    context = {
        'user': User.objects.get(id=profile_id)
    }
    return render(request, "user_profile.html", context)