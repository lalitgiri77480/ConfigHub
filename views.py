from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def index(request):
    return render(request,'accounts/index.html')
    
def signUp(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        unm = request.POST['unm']
        pwd = request.POST['pwd']
        try :
            user = User.objects.get(username=unm)
            return render(request,'accounts/signup.html',{'error':"User Already Exists."})
        except:
            user = User.objects.create_user(first_name = fname,last_name=lname,email=email,username=unm,password=pwd)
            user.save()
            return render(request,'accounts/signup.html',{'msg':"User Registerd Successfully."})
    else:
        return render(request,'accounts/signup.html')

def signIn(request):
    if request.method == "POST":
        unm = request.POST['unm']
        pwd = request.POST['pwd']
        user = auth.authenticate(username = unm,password = pwd)
        if user is not None:
            auth.login(request,user)
            return render(request,"accounts/userhome.html")
        else:
            return render(request,'accounts/signin.html',{'error':"Invalid Username or Password."})
    else:
        return render(request,'accounts/signin.html',{'error':"Invalid User Request."})


def signOut(request):
    auth.logout(request)
    return render(request,'accounts/signin.html',{'msg':"Logout Successfully."})
