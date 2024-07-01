# urls.py
from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path("", views.student_list, name="student_list"),
    path("create/", views.create_students, name="create_students"),
    path("edit/<int:student_id>/", views.edit_students, name="edit_students"),
]
