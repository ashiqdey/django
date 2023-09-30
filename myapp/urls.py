from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),  # Example app-specific URL pattern
    # Define other app-specific URL patterns here
]