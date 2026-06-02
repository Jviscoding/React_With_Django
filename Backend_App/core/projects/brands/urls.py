from django.urls import path
from .views import brands

urlpatterns = [
    path("brands/", brands),
]