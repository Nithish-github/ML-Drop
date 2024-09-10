import os
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage
from .forms import UploadFilesForm
from .ml.yolo_training import train_yolo_model  # Import your YOLO training function
from rest_framework.views import APIView
from django.core.files.base import ContentFile



def index(request):
    return HttpResponse("YOLO Model Training")

class UploadView(APIView):

    def get(self, request):
        form = UploadFilesForm()
        return render(request, 'upload.html', {'form': form})

    def post(self, request):
        form = UploadFilesForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded files
            images_folder = request.FILES.getlist('images_folder')
            labels_folder = request.FILES.getlist('labels_folder')
            classes_file = request.FILES['classes_file']
            
            image_paths = []
            label_paths = []

            for image in images_folder:
                path = default_storage.save(f'uploads/images/{image.name}', ContentFile(image.read()))
                image_paths.append(path)
            
            for label in labels_folder:
                path = default_storage.save(f'uploads/labels/{label.name}', ContentFile(label.read()))
                label_paths.append(path)

            classes_path = default_storage.save(f'uploads/{classes_file.name}', ContentFile(classes_file.read()))

            # Call the YOLO training function with the paths
            result = train_yolo_model(image_paths, label_paths, classes_path)

            return HttpResponse(f"Training completed: {result}")
        return HttpResponse("Invalid form data", status=400)
