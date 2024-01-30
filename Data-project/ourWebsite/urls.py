from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("universities/", views.universities, name="universities"),
    path("home/", views.index, name="home"),

]
