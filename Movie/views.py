from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from Movie.models import Product, Product_info,MovieBook


def show(request):
    movies=Product.objects.all()

    return render(request,"Website/movies.html",{'Movie':movies})


@login_required(login_url="/login")
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
        avTickets=request.POST['avSeats']
        if int(quantity)>int(avTickets):
            return HttpResponse("There is only "+str(avTickets)+" remaining!!")

        else:
            update=Product_info.objects.get(product=pid)
            update.AvailableSeats=int(avTickets)-int(quantity)
            update.save()
            obj = MovieBook(movie_name=movie_name, username=username, type=type, quantity=quantity, price=price,BookedDate=date,ExpiryDate=expired_date,time=time)

            obj.save()
            messages.info(request, "INFO: Your Booking is done")
            return redirect("/mytickets")



    movieBook=Product_info.objects.get(product=pid)

    return render(request,"Website/singlemovie.html",{"Movie":movieBook})