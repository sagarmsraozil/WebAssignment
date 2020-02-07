from django.urls import path

from practiceApp import views

urlpatterns=[
    path("",views.show),
    path("Login/",views.log),
    path("movie/",views.movie),
    # path("<pid>",views.singleMovie)
]