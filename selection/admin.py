from django.contrib import admin

from .models import Teacher, Student, Topic
# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Topic)
