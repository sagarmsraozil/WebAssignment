from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from Home.models import Home


def show(request):
    index_element=Home.objects.all()

    return render(request,"Website/index.html",{"first":index_element})

def register(request):
    if request.method  =='POST':
        fn=request.POST['fname']
        ln=request.POST['lname']
        em=request.POST['email']
        un=request.POST['uname']
        pw=request.POST['password']
        user=User.objects.create_user(first_name=fn, last_name=ln,email=em,username=un,password=pw)
        user.save()
        return redirect("/Home/login")
    return render(request,"Website/register.html")


def login(request):
    if request.method=="POST":
        un = request.POST['username']
        pw = request.POST['password']
        user=auth.authenticate(username=un, password=pw)

        if user is not None:
            auth.login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/Home')
        else:
            return HttpResponse("False")
    return render(request, "Website/login.html")







def logout(request):
    auth.logout(request)
    return redirect('/Home/login')
