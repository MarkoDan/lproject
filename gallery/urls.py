from django.urls import path 
from .views import image_upload, image_list

urlpatterns = [
    path('upload/', image_upload, name='upload'),
    path('images/', image_list, name='image_list'),
]