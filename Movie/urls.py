from django.urls import path

from Movie import views

urlpatterns=[
    path("",views.show),
    path("<pid>",views.Book)
]