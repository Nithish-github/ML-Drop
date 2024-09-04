from django.shortcuts import render
from django.http import HttpResponse


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import base64
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


# Create your views here.

def index(reponse):
    return HttpResponse("IM Back")

def index_2(reponse):
    return HttpResponse("IM Back fucker")


class ExampleView(APIView):
    def get(self, request):

        data = {"message": "Hello from backend!"}

        # Path to your image
        image_path = "/home/nkumar/griffyn/ML-Drop/mypage/assests/kobe-lebron-nbajpg.jpg"
        
        # Open the image and encode it to Base64
        with open(image_path, "rb") as img_file:
            encoded_image = base64.b64encode(img_file.read()).decode('utf-8')

        data = {
            "message": "Hello from backend!",
            "image_data": encoded_image
        }
        return Response(data, status=status.HTTP_200_OK)

    
    def post(self, request):
        # Access the data sent in the request
        received_data = request.data
        print("Received POST data:", received_data)
        
        # You can process the received data here
        response_data = {"message": "Data received", "received_data": received_data}
        
        # Return a response with the received data
        return Response(response_data, status=status.HTTP_201_CREATED)

