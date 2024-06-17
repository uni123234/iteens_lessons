from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('create_students/', views.create_students, name='create_students'),
]
