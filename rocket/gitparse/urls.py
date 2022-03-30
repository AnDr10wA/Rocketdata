from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', GitParse.as_view(), name = 'git_parse'),
    path('project', ProjectListView.as_view()),
    path('repos/<str:project>', ReposListView.as_view()),
    path('stats', StatsView.as_view()),
    path('statsone/<str:project>', StatsOneView.as_view())



]