from django.urls import path
from . import views

urlpatterns = [
    path('homes/', views.homes, name="homes"),
    path('abouts/', views.abouts, name="abouts")
]