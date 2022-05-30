from django.urls import path
from . import views

urlpatterns = [
    # represents root of the application
    path('', views.index),
    path('new', views.new),
]