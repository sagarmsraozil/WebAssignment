from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from Movie.models import MovieBook, Product_info


@login_required(login_url='/login')

def show(request):
    if request.method=="POST":
        mid=request.POST['id']
        movie_id=request.POST['movieId']
        print(movie_id)
        obj1=Product_info.objects.get(product=movie_id)
        obj=MovieBook.objects.get(id=mid)
        a=int(obj.quantity)

        obj.type=request.POST['type']
        obj.ExpiryDate=request.POST['date']
        obj.time=request.POST['time']
        obj.quantity=request.POST['no']
        obj1.AvailableSeats = int(obj1.AvailableSeats) - int(obj.quantity) + a
        obj.price = request.POST['price']
        if int(obj1.AvailableSeats)<(int(obj.quantity)-a):
            return HttpResponse("You have only "+str(obj1.AvailableSeats)+" remaining!!")
        else:



            obj1.save()
            obj.save()

    tickets=MovieBook.objects.filter(username=request.user).order_by('ExpiryDate')
    return render(request,"Website/mytickets.html",{"ticket":tickets})

def delete(request,pid):
    obj=MovieBook.objects.get(id=pid)
    obj.delete()
    return redirect('/mytickets')







