from django.contrib import admin

# Register your models here.
from About.models import About

class Aboutadmin(admin.ModelAdmin):
    list_display = ("our_team","sponsors","aim")

admin.site.register(About,Aboutadmin)
