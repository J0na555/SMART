from django.contrib import admin
from .models import Student, Semester, Grade, AcademicYear, Assessment, Mark, Subject, Teacher


admin.site.register(Subject)
admin.site.register(Semester)
admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(AcademicYear)
admin.site.register(Mark)
admin.site.register(Assessment)
admin.site.register(Teacher)