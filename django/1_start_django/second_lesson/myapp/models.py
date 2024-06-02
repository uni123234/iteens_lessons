from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    school_number = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

class Class(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    class_number = models.CharField(max_length=10)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"Class {self.class_number} at {self.school.name}"

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    class_number = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
