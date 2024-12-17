# responses/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('simple_response/', views.simple_response, name='simple_response'),
    path('json_response/', views.json_response, name='json_response'),
    path('stream_response/', views.stream_response, name='stream_response'),
    path('file_response/', views.file_response, name='file_response'),
    path('html_response/', views.html_response, name='html_response'),
    path('xml_response/', views.xml_response, name='xml_response'),
    path('plain_text_response/', views.plain_text_response, name='plain_text_response'),
    path('json_list_response/', views.json_list_response, name='json_list_response'),
    path('image_response/', views.image_response, name='image_response'),
    path('video_response/', views.video_response, name='video_response'),
]