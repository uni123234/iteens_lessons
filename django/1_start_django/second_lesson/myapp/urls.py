from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'myapp'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='myapp:login'), name='logout'),
    path('', views.student_list, name='student_list'),
    path('create/', views.create_students, name='create_students'),
    path('edit/<int:student_id>/', views.edit_students, name='edit_students'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/create/', views.create_teacher, name='create_teacher'),
    path('teachers/edit/<int:teacher_id>/', views.edit_teacher, name='edit_teacher'),
    path('search_teacher_name/', views.search_teacher_name, name='search_teacher_name'),  # Teacher search
    path('search_student_name/', views.search_student_name, name='search_student_name'),  # Student search
]
