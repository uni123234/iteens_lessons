from django import forms
from .models import Student, School, Class

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'address', 'school', 'class_number']
