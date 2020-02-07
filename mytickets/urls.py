from django.urls import path

from mytickets import views

urlpatterns = [
    path("",views.show),
    path("update/<pid>",views.update),
    path("delete/<pid>",views.delete)
]
