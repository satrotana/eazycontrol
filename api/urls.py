from django.urls import path
from .views import *

urlpatterns = [
    path('membershiplistview/<str:cm>;<str:fid>', membershipListView),
]
