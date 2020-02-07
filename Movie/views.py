from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from Movie.models import Product, Product_info,MovieBook


def show(request):
    movies=Product.objects.all()

    return render(request,"Website/movies.html",{'Movie':movies})


@login_required(login_url="/Home/login")
def Book(request,pid):
    if request.method=="POST":
        movie_name=Product.objects.get(id=pid)
        type=request.POST['type']
        quantity = request.POST['no']
        username=request.user
        date=datetime.now()
        expired_date=request.POST['date']
        time=request.POST['time']
        price=request.POST['price']
        obj = MovieBook(movie_name=movie_name, username=username, type=type, quantity=quantity, price=price,BookedDate=date,ExpiryDate=expired_date,time=time)

        obj.save()
        return redirect("/mytickets")
    movieBook=Product_info.objects.get(product=pid)

    return render(request,"Website/singlemovie.html",{"Movie":movieBook})