from django.db import models

# Create your models here.

class About(models.Model):
    our_team=models.TextField()
    sponsors=models.TextField()
    aim=models.TextField()

