from django.shortcuts import render
from .models import School, Class, Student

def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})