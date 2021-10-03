from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from stock.functions import *

@login_required(login_url='login')
def home(request):
    userInfo = MemberControl('S',str(request.user.id),'ALL')
    return render(request, 'home.html',{'userInfo':userInfo})

def loginUser(request):
    message =''
    if request.method == 'POST':
        Gusername = request.POST['userName']
        Gpassword = request.POST['password']

        findUser = User.objects.filter(username = Gusername)

        if Gusername == '' and Gpassword == '':
            message = 'Your username and password are empty!'
        elif Gpassword == '':
            message = 'Your password is empty!'
        elif Gusername == '':
            message = 'Your username is empty!'
        elif Gusername is not None and Gpassword is not None:
            if findUser:
                request.session.set_expiry(0)
                user = authenticate(request, username = Gusername, password = Gpassword)
                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    message = 'Your password is incorrect!'
                    return render(request,'auth/login.html',{'message':message,'field_username':Gusername})
            else:
                message = 'Your username is not exists!'
                return render(request,'auth/login.html',{'message':message})
    return render(request, 'auth/login.html',{'message':message})

def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):
    message = ''
    if request.method == 'POST':
        Gusername = request.POST['userName']
        Gfirstname = request.POST['firstName']
        Glastname = request.POST['lastName']
        Gemail = request.POST['email']
        Gpass1 = request.POST['password1']
        Gpass2 = request.POST['password2']

        form_data ={
            'field_username':Gusername,
            'field_firstname':Gfirstname,
            'field_lastname':Glastname,
            'field_Gemail':Gemail,
        }

        if Gusername == '' and Gfirstname == '' and Glastname == '' and Gemail == '' and Gpass1 == '' and Gpass2 == '':
            message = 'Please fill all requirment!'
        elif Gusername == '':
            message ='Your username is empty!'
        elif Gfirstname == '':
            message ='Your first name is empty!'
        elif Glastname == '':
            message ='Your last name is empty!'
        elif Gemail == '':
            message ='Your Gmail is empty!'
        elif Gpass1 == '':
            message ='Your password is empty!'
        elif Gpass2 == '':
            message ='Your confirm password is empty!'
        elif len(Gpass1) < 6:
            message ='Password can not less than 6 digit!'
        else:
            findUser = User.objects.filter(username = Gusername)
            findGmail = User.objects.filter(email = Gemail)
            if findUser:
                message = "Your username '"+Gusername+"' is exists please try with another username!"
                return render(request, 'auth/register.html',{'message':message,'form_data':form_data})
            elif findGmail:
                message = "Your email address '"+Gemail+"' is ready in use, please try with another email address!"
                return render(request, 'auth/register.html',{'message':message,'form_data':form_data})
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
                    message = 'Your password not match!'
                    return render(request, 'auth/register.html',{'message':message,'form_data':form_data}) 
        return render(request, 'auth/register.html',{'message':message,'form_data':form_data})
    else :
        return render(request, 'auth/register.html')

def changepassword(request):
    return render(request,'auth/changepass.html')

# Members ---------------------------------------------------------------------
@login_required(login_url='login')
def membership(request):
    resp = MemberControl('S','ALL','0')
    userInfo = MemberControl('S',str(request.user.id),'ALL')
    return render(request, "membership/memberlist.html",{'data':resp,'userInfo':userInfo})

def memberinput(request):
    userInfo = MemberControl('S',str(request.user.id),'ALL')
    return render(request, "membership/inputform.html",{'userInfo':userInfo})

@login_required(login_url='login')
def memberprofile(request,id):
    userInfo = MemberControl('S',str(request.user.id),'ALL')
    GetuserInfo = MemberControl('S',str(id),'ALL')
    print(GetuserInfo)
    return render(request,'membership/profiles.html',{'userInfo':userInfo,'GetuserInfo':GetuserInfo})

# Staffs ---------------------------------------------------------------------
@login_required(login_url='login')
def stafflist(request):
    resp = MemberControl('S','ALL','1')
    userInfo = MemberControl('S',str(request.user.id),'ALL')
    return render(request, "staffs/stafflist.html",{'data':resp,'userInfo':userInfo})

@login_required(login_url='login')
def grouppermission(request):
    userInfo = MemberControl('S',str(request.user.id),'ALL')
    return render(request, "staffs/grouppermission.html",{'userInfo':userInfo})

@login_required(login_url='login')
def permissionsetting(request):
    resp = MemberControl('S','ALL','ALL')
    userInfo = MemberControl('S',str(request.user.id),'ALL')
    return render(request, "staffs/permissionsetting.html",{'data':resp,'userInfo':userInfo})

@login_required(login_url='login')
def bookstore(request):
    userInfo = MemberControl('S',str(request.user.id),'ALL')
    return render(request, "bookstore/bookstore.html",{'userInfo':userInfo})

# Books ---------------------------------------------------------------------
@login_required(login_url='login')
def bookdetail(request,id):
    userInfo = MemberControl('S',str(request.user.id),'ALL')
    return render(request, "bookstore/bookdetail.html",{'userInfo':userInfo})

@login_required(login_url='login')
def updatebook(request,id):
    userInfo = MemberControl('S',str(request.user.id),'ALL')
    return render(request, "bookstore/inputform.html",{'userInfo':userInfo})

@login_required(login_url='login')
def insertbook(request):
    userInfo = MemberControl('S',str(request.user.id),'ALL')
    return render(request, "bookstore/inputform.html",{'userInfo':userInfo})

@login_required(login_url='login')
def borrowbook(request):
    userInfo = MemberControl('S',str(request.user.id),'ALL')
    return render(request, "bookstore/borrowingbook.html",{'userInfo':userInfo})

@login_required(login_url='login')
def borrowedlist(request):
    userInfo = MemberControl('S',str(request.user.id),'ALL')
    return render(request, "bookstore/borrowedlist.html",{'userInfo':userInfo})

@login_required(login_url='login')
def returnbook(request):
    userInfo = MemberControl('S',str(request.user.id),'ALL')
    return render(request, "bookstore/returnlist.html",{'userInfo':userInfo})

@login_required(login_url='login')
def booksetting(request):
    userInfo = MemberControl('S',str(request.user.id),'ALL')
    return render(request, "bookstore/settings.html",{'userInfo':userInfo})

# Ques ---------------------------------------------------------------------
@login_required(login_url='login')
def questionlist(request):
    userInfo = MemberControl('S',str(request.user.id),'ALL')
    return render(request, "ques/questionlist.html",{'userInfo':userInfo})

@login_required(login_url='login')
def insertQuesAnser(request):
    userInfo = MemberControl('S',str(request.user.id),'ALL')
    return render(request, "ques/inputform.html",{'userInfo':userInfo})