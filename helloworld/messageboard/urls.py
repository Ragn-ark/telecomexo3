# messageboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('submit_message/', views.submit_message, name='submit_message'),
    path('get_messages/', views.get_messages, name='get_messages'),
]
