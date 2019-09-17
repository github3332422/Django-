from django.contrib import admin
from .models import *
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','student_name','student_major','student_age','teacher')
    fields = ('student_name','student_major','student_age','teacher')

admin.site.register(Student,StudentAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher_name', 'teacher_major', 'teacher_age')
    ordering = ('-id',)
    list_per_page = 5
    list_editable = ('teacher_age',)
    readonly_fields = ('teacher_major',)
    fields = ('teacher_name', 'teacher_major', 'teacher_age')

admin.site.register(Teacher,TeacherAdmin)

