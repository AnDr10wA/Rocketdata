from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', GitParse.as_view(), name = 'git_parse'),
    # path('create', NewsCreate.as_view(), name = 'news_create_url'),
    # path('<str:slug>', NewsDetail.as_view(), name = 'news_detail_url'),


]