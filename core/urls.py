from django.urls import path

from .views import index, concact


urlpatterns = [
    path('', index),
    path('contact/', concact),
]