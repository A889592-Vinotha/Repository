from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_note, name='create_note'),
    # Add more URL patterns as needed
]