from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from Movie.models import Product


def show(request):
    if request.method=="POST":
        fn=request.POST['fn']
        ln = request.POST['ln']
        email = request.POST['email']
        username = request.POST['un']
        password = request.POST['pw']

        user=User.objects.create_user(first_name=fn, last_name=ln, email=email, username=username, password=password)
        user.save()

    return render(request, "practice/register.html")


def log(request):
    if request.method=="POST":
        un=request.POST['un']
        pw=request.POST['pw']

        user=auth.authenticate(username=un,password=pw)
        if user is not None:
            auth.login(request,user)
            return redirect("/Practice")
        else:
            return HttpResponse("<script> alert('Error')  </script> ")

    return render(request,"Practice/login.html")


def movie(request):
    products=Product.objects.all()
    return render(request, "Practice/movie.html", {"Products":products})

#
# def singleMovie(request, pid):
#     pr = Product_info.objects.filter(product=pid)
#     return render(request, "Practice/singleMovie.html", {"Product": pr})








