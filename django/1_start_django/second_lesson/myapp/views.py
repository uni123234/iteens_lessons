# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import School, Class, Student
from .forms import StudentForm


def student_list(request):
    students = Student.objects.all()
    return render(request, "index.html", {"students": students})


def create_students(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("myapp:student_list")
    else:
        form = StudentForm()
    return render(request, "create_students.html", {"form": form})


def edit_students(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("myapp:student_list")
    else:
        form = StudentForm(instance=student)
    return render(request, "edit_students.html", {"form": form})
