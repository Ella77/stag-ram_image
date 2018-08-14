"""stagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from photos.views import hello, detail,create
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^hello/$', hello),
    url(r'^photos/(?P<pk>[0-9]+)/$', detail, name='detail'),
    url(r'^photos/upload/$', create, name='create'),
    url('accounts/login/', auth_views.LoginView.as_view(),name='login')
    ,
    url('accounts/logout/', auth_views.LogoutView.as_view(),name='logout')
    ,
    url(r'^users/',include('profiles.urls')),



]

urlpatterns+= static('/upload_files/', document_root=settings.MEDIA_ROOT)