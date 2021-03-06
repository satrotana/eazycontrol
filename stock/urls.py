from django.urls import path
from .views import *

urlpatterns = [
    path('', home,name='home'),
    path('login', loginUser,name='login'),
    path('logout', logoutUser,name='logout'),
    path('register', register,name='register'),

    path('memberlist', membership,name='memberlist'),
    path('memberinput', memberinput,name='memberinput'),
    
    path('stafflist', stafflist,name='stafflist'),
    path('changepass', changepassword,name='changepass'),
    path('profile/<str:id>', memberprofile, name = 'profile'),
    path('grouppermission', grouppermission,name='grouppermission'),
    path('permissionsetting', permissionsetting,name='permissionsetting'),

    path('bookstore', bookstore,name='bookstore'),
    path('bookdetail/<str:id>', bookdetail),
    path('updatebooks/<str:id>', updatebook),
    path('inputbooks', insertbook,name='inputbooks'),
    path('borrowbook', borrowbook,name='borrowbook'),
    path('borrowedlist', borrowedlist,name='borrowedlist'),
    path('returnbook', returnbook,name='returnbook'),
    path('booksetting', booksetting,name='booksetting'),

    path('questionlist', questionlist,name='questionlist'),
    path('insertQuesAnser', insertQuesAnser,name='insertQuesAnser'),
]
