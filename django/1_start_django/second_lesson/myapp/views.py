from django.shortcuts import render
from .models import School, Class, Student

def student(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})