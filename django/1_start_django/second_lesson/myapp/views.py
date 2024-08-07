from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import School, Class, Student, CustomUser, Teacher
from .forms import StudentForm, UserLoginForm, CustomUserCreationForm, TeacherForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("email")
            messages.success(request, f"Account created for {username}!")
            login(request, user)
            return redirect("myapp:student_list")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect("myapp:student_list")
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = UserLoginForm()
    return render(request, "login.html", {"form": form})


@login_required
def student_list(request):
    students = Student.objects.all()
    paginator = Paginator(students, 10)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)
    return render(request, "index.html", {"page_obj": page_obj})


@login_required
def teacher_list(request):
    teachers = Teacher.objects.all()
    paginator = Paginator(teachers, 10)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)
    return render(request, "teacher_list.html", {"page_obj": page_obj})


@login_required
def create_students(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("myapp:student_list")
    else:
        form = StudentForm()
    return render(request, "create_students.html", {"form": form})


@login_required
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


@login_required
def create_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("myapp:teacher_list")
    else:
        form = TeacherForm()
    return render(request, "create_teacher.html", {"form": form})


@login_required
def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect("myapp:teacher_list")
    else:
        form = TeacherForm(instance=teacher)
    return render(request, "edit_teacher.html", {"form": form})


def search_name(request):
    query = request.GET.get('query', '')
    if query:
        students = Student.objects.filter(name__icontains=query).values_list('name', flat=True)
        teachers = Teacher.objects.filter(name__icontains=query).values_list('name', flat=True)
        results = list(students) + list(teachers)
        return JsonResponse(results, safe=False)
    return JsonResponse([], safe=False)
