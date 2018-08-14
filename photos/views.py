from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Photo
from .forms import PhotoForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# Create your views here.


def hello(request):
    return HttpResponse('안녕하세요!')

def detail(request, pk):

    photo = get_object_or_404(Photo, pk=pk)
    messages = (
        '<p>{pk}번 사진 보여줄게요</p>'.format(pk=photo.pk),
        '<p>주소는 {url}</p>'.format(url=photo.image.url),
        '<p><img src ="{url}" /></p>'.format(url=photo.image.url),
    )
    return HttpResponse('\n'.join(messages))

@login_required
def create(request):

    if request.method=="GET":
        form = PhotoForm()
    elif request.method =="POST":
        form = PhotoForm(request.POST,request.FILES,request.user)
        if form.is_valid():
            obj =form.save(commit=False)
            obj.user=request.user
            obj=form.save()
            return redirect(obj)
            #get_absolute_url
    ctx = {
        'form':form,
    }
    return render(request,'edit.html',ctx)

def profile(request,username):
    User = get_user_model()
    user = get_object_or_404(User,username=username)
    photos = user.photo_set.order_by('-created at','-pk')

    ctx = {
        'user':user,
        'photos':photos,
    }
    return render(request,'profile.html',ctx)
#
# def homepage(request):
#     return redirect('/accounts/login/')