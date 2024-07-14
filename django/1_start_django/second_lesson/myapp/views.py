from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import School, Class, Student, CustomUser, Teacher
from .forms import StudentForm, UserLoginForm, CustomUserCreationForm, TeacherForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('myapp:student_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('myapp:student_list')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, "index.html", {"students": students})

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
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teacher_list.html", {"teachers": teachers})

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


def search_teacher_name(request):
    query = request.GET.get('query', '')
    if query:
        teachers = Teacher.objects.filter(first_name__icontains=query) | Teacher.objects.filter(last_name__icontains=query)
        names = [f"{teacher.first_name} {teacher.last_name}" for teacher in teachers]
    else:
        names = []
    return JsonResponse(names, safe=False)


def search_student_name(request):
    query = request.GET.get('query', '')
    if query:
        students = Student.objects.filter(first_name__icontains=query) | Student.objects.filter(last_name__icontains=query)
        names = [f"{student.first_name} {student.last_name}" for student in students]
    else:
        names = []
    return JsonResponse(names, safe=False)