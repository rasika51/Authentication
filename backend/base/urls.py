from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),  # Add this route
]
