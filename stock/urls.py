from django.urls import path
from .views import *

urlpatterns = [
    path('', home,name='home'),
    path('login', loginUser,name='login'),
    path('logout', logoutUser,name='logout'),
    path('register', register,name='register'),
    path('memberlist', membership,name='memberlist'),
    # path('registerHttp', registerNew,name='registerHttp'),
]
