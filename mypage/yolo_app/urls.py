from django.urls import path
from . import views
urlpatterns = [
    path('upload/', views.UploadView, name='upload_files'),
]
