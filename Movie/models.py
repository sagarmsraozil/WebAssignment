from datetime import datetime, date

from django.conf import settings
from django.db import models


# Create your models here.


class Product(models.Model):
    image = models.FileField()
    movie_name = models.CharField(max_length=50)

    def __str__(self):
        return self.movie_name

class Product_info(models.Model):
    description = models.TextField()
    title_img = models.FileField(blank=True)
    img1 = models.FileField(blank=True)
    img2 = models.FileField(blank=True)
    img3 = models.FileField(blank=True)
    img4 = models.FileField(blank=True)
    AvailableSeats=models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default="")

class MovieBook(models.Model):
    movie_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    quantity = models.IntegerField()
    price = models.IntegerField()
    time=models.CharField(default="",max_length=40)
    BookedDate = models.DateField()
    ExpiryDate = models.DateField()
