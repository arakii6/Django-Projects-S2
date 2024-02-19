from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Department)
admin.site.register(StudentId)
admin.site.register(Student)
admin.site.register(Subject)

# Define a custom admin for Subject_Marksc
class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ['student','subject','marks']

# Register the custom admin for Subject_Marks
admin.site.register(SubjectMarks, SubjectMarksAdmin)


class Report_Card_Admin(admin.ModelAdmin):

    ordering = ['rank']
    list_display = ['student','total','rank']


admin.site.register(Report_Card,Report_Card_Admin)
