from django.contrib import admin

# Register your models here.
from Home.models import Home


class Adminhome(admin.ModelAdmin):
    list_display = ("img","description")

admin.site.register(Home,Adminhome)
