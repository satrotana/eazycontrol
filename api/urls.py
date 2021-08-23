from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('membershiplistview/', membershipListView),
    path('membershiplistview/<int:pk>', membershipDetailView),
]