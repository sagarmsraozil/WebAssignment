from django.urls import path

from mytickets import views

urlpatterns = [
    path("",views.show),

    path("delete/<pid>",views.delete)
]
