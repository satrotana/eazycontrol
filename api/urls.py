from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('membershiplistview/<str:cm>;<str:fid>', membershipListView),
    # path('membershiplistview/<str:fid>', membershipDetailView),
]
