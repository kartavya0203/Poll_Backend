"""
URL configuration for polls project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import *

urlpatterns = [
path('polls/',PollList.as_view(),name='polls_list'),
path('polls/<int:pk>/',PollDetail.as_view(),name='polls_detail'),
path('choices/',ChoiceList.as_view(),name='choice_list'),
path('vote/',CreateVote.as_view(),name='create_vote'),
path('usersignup/',UserView.as_view(),name='user_create'),
path('Login/',LoginApiView.as_view(),name='login')
]