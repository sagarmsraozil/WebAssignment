from django.db import models

# Create your models here.

class Home(models.Model):
    img=models.CharField(max_length=2086)

    description=models.TextField()

