from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

# Create your views here.


def profile(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    ctx ={
        'user' : user,
    }
    return render(request, 'profile.html',ctx)