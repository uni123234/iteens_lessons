from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import School, Class, Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

def create_students(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:student_list')
    else:
        form = StudentForm()
    return render(request, 'create_students.html', {'form': form})
