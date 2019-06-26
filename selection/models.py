from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from thesis.storage_backends import MediaStorage
# Create your models here.
class Student(models.Model):
    person = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    number = models.CharField(max_length=64)
    class_name = models.CharField(max_length=64)
    gpa = models.CharField(max_length=64, null=True, blank=True)
    def __str__(self):
        return f"{self.number} {self.person.username} {self.class_name}"

class Teacher(models.Model):
    person = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    degree = models.CharField(max_length=64, null=True)
    title = models.CharField(max_length=64, null=True)
    major = models.CharField(max_length=256, null=True)
    uni =  models.CharField(max_length=64, null=True)
    image = models.ImageField(null=True)
    def __str__(self):
        return f"{self.person.username} {self.title}"

class Topic(models.Model):
    title = models.CharField(max_length=256, null=True)
    req = models.CharField(max_length=256, null=True)
    output = models.CharField(max_length=256, null=True)
    tool = models.CharField(max_length=256, null=True)
    giver = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="supervisor")
    taker = models.ManyToManyField(Student, blank=True, related_name="author")

    def __str__(self):
        return f"{self.title} author: {self.taker.all()}, supervisor: {self.giver}"

class TeacherImage(ModelForm):
    degree = forms.CharField(required=False)
    title = forms.CharField(required=False)
    major = forms.CharField(required=False)
    uni =  forms.CharField(required=False)
    image = forms.ImageField(required=False)
    class Meta:
        model = Teacher
        fields = '__all__'
