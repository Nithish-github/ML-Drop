from django.urls import path

from . import views

urlpatterns = [
    path("janauary",views.index),
    path("feb",views.index_2),
    path('api/example/', views.ExampleView.as_view(), name='example-api'),

]