from enum import auto
from inspect import findsource
from django.conf.urls import url
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
import requests

EZapi = 'http://127.0.0.1:8000/ezapi/'

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

def loginUser(request):
    if request.method == 'POST':
        Gusername = request.POST['userName']
        Gpassword = request.POST['password']

        findUser = User.objects.filter(username = Gusername)

        if findUser:
            request.session.set_expiry(300)
            user = authenticate(request, username = Gusername, password = Gpassword)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request,'auth/login.html',{'message':'Your password is incorrect!'})
        else:
            return render(request,'auth/login.html',{'message':'Your username is not exists!'})
    return render(request, 'auth/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        Gusername = request.POST['userName']
        Gfirstname = request.POST['firstName']
        Glastname = request.POST['lastName']
        Gemail = request.POST['email']
        Gpass1 = request.POST['password1']
        Gpass2 = request.POST['password2']

        findUser = User.objects.filter(username = Gusername)
        msg = "Your username '"+Gusername+"' is exists please try with other username!"

        if findUser:
            return render(request, 'auth/register.html',{'message':msg})
        else:
            if Gusername == '' or Gfirstname == '' or Glastname == '' or Gemail == '' or Gpass1 == '' or Gpass2 == '':
                return render(request, 'auth/register.html',{'message':'Please field all information bellow !'}) 
            else:
                if Gpass1 ==  Gpass2:
                    newRegister = User.objects.create(
                        username = Gusername,
                        first_name = Gfirstname,
                        last_name = Glastname,
                        email = Gemail,
                        password = make_password(Gpass1)
                    )
                    newRegister.save()
                    return redirect('login')
                else:
                    return render(request, 'auth/register.html',{'message':'Your password not match!'}) 
    else :
        return render(request, 'auth/register.html')

def membership(request):
    params = dict(
        origin='Chicago,IL',
        destination='Los+Angeles,CA',
        waypoints='Joplin,MO|Oklahoma+City,OK',
        sensor='false'
    )
    resp = requests.get(url=EZapi+"membershiplistview", params=params)
    data = resp.json()
    return render(request, "membership/memberlist.html",{'data':data})
