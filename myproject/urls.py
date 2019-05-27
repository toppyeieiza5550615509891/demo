"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from myapp import views
from myapp.views import (blog, blog_item, addblog, profile, auth, signup, signout, test)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth.as_view(),  name='auth'),
    path('blog/',blog.as_view(), name='blog'),
    
    path('blog/<int:pk>', blog_item.as_view(), name='blog_id'),
    path('blog/addblog', addblog.as_view(), name='addblog'),
    path('signup', signup.as_view(), name='signup'),
    path('blog/signout', signout.as_view()),
    path('profile', profile.as_view(), name='profile'),
    path('test', test.as_view())
]