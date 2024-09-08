from django.shortcuts import render
from django.http import HttpResponse


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import cv2
import numpy as np
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

        # Get base64-encoded image and filter type
        base64_image = received_data.get('image_base64')
        filter_type = received_data.get('filter_type')

        if not base64_image or not filter_type:
            return Response({"error": "Image and filter type are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Decode the base64 image
        image_data = base64.b64decode(base64_image)
        np_image = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(np_image, cv2.IMREAD_COLOR)

        # Apply the specified filter
        if filter_type == 'gray':
            processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        elif filter_type == 'blur':
            processed_image = cv2.GaussianBlur(image, (5, 5), 0)
        else:
            return Response({"error": "Invalid filter type provided."}, status=status.HTTP_400_BAD_REQUEST)

        # Encode the processed image back to base64
        _, buffer = cv2.imencode('.jpg', processed_image)
        processed_image_base64 = base64.b64encode(buffer).decode('utf-8')

        # Response data
        response_data = {
            "message": "Data received and processed",
            "processed_image_base64": processed_image_base64
        }

        # Return a response with the processed image
        return Response(response_data, status=status.HTTP_201_CREATED)