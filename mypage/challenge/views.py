from django.shortcuts import render
from django.http import HttpResponse


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def index(reponse):
    return HttpResponse("IM Back")

def index_2(reponse):
    return HttpResponse("IM Back fucker")


class ExampleView(APIView):
    def get(self, request):
        data = {"message": "Hello from Django!"}
        return Response(data, status=status.HTTP_200_OK)

