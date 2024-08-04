from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(reponse):
    return HttpResponse("IM Back")

def index_2(reponse):
    return HttpResponse("IM Back fucker")
