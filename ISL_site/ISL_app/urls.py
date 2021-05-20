"""ISL_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from .views import *


urlpatterns = [
    # path('/home', home ,name='home'),
    path('k/', camera, name="camera"),
    path('', index, name="index"),
    path('signin/index', index, name="index"),
    path('signup/index', index, name="index"),
    path('signin/', signin , name="signin"),
    path('signup/', signup , name="signup"),
    path('signin/signin', signin , name="signin"),
    path('signup/signup', signup , name="signup"),
    path('signin/signup', signup , name="signup"),
    path('signup/signin', log , name="log"),
    path('signin/log', log , name="log"),
    path('signup/log', log , name="log"),
    path('log/', log , name='log'),
    path('feedback/',index , name='index'),
    path('findhand/', findhand ,  name="findhand"),
    path('sample', sample ,  name="sample")
            ]
