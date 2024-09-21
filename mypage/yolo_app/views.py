import os
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage
from .forms import UploadFilesForm
from .ml.yolo_training import train_yolo_model  # Import your YOLO training function
from rest_framework.views import APIView
from django.core.files.base import ContentFile
from django.template import loader

def index(request):
    return HttpResponse("YOLO Model Training")


class UploadView(APIView):

    def get(self, request):
        form = UploadFilesForm()
        # Correcting the template path to use relative path as expected in Django
        context = {'form': form}  # Pass the form in the context
        template = loader.get_template('upload.html')
        
        return HttpResponse(template.render(context, request))

    def post(self, request):
        form = UploadFilesForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle uploaded files
            images_folder = request.FILES.getlist('images_folder')
            labels_folder = request.FILES.getlist('labels_folder')
            classes_file = request.FILES.get('classes_file')
            
            image_paths = []
            label_paths = []

            # Save images
            for image in images_folder:
                path = default_storage.save(f'uploads/images/{image.name}', ContentFile(image.read()))
                image_paths.append(path)
            
            # Save labels
            for label in labels_folder:
                path = default_storage.save(f'uploads/labels/{label.name}', ContentFile(label.read()))
                label_paths.append(path)

            # Save classes file
            if classes_file:
                classes_path = default_storage.save(f'uploads/{classes_file.name}', ContentFile(classes_file.read()))
            else:
                return HttpResponse("Classes file is missing", status=400)

            # Call the YOLO training function with the saved file paths
            try:
                result = train_yolo_model(image_paths, label_paths, classes_path)
                return HttpResponse(f"Training completed: {result}")
            except Exception as e:
                return HttpResponse(f"Error during training: {str(e)}", status=500)

        return HttpResponse("Invalid form data", status=400)
