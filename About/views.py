from django.shortcuts import render

# Create your views here.
from About.models import About


def show(request):
    descriptions=About.objects.all()
    return render(request,"Website/aboutUs.html",{"description":descriptions})