from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from Movie.models import MovieBook


@login_required(login_url='/Home/login')

def show(request):
    tickets=MovieBook.objects.filter(username=request.user)
    return render(request,"Website/mytickets.html",{"ticket":tickets})

def delete(request,pid):
    obj=MovieBook.objects.get(id=pid)
    obj.delete()
    tickets=MovieBook.objects.filter(username=request.user)
    return render(request,"Website/mytickets.html",{"ticket":tickets})

def update(request,pid):
    seat=MovieBook.objects.get(id=pid)

    if request.method=="POST":
        pass

    obj=MovieBook.objects.filter(username=request.user)
    return render(request,"Websites/mytickets.html",{"ticket":obj})
