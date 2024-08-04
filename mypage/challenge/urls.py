from django.urls import path

from . import views

urlpatterns = [
    path("janauary",views.index),
    path("feb",views.index_2)
]