from django.shortcuts import render
from urllib import request
from django.db.models import Count, Q
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from .models import Student, Mark, Attendace, Grade, Subject, Teacher
from django.urls import reverse_lazy


class StudentListView(ListView):
    model = Student
    template_name = 'tracker/student_list.html'
    context_object_name = 'students'


class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'tracker/student_form.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'tracker/student_form.html'
    success_url = reverse_lazy('student-list')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'tracker/student_confirm_delete.html'
    success_url = reverse_lazy('student-list')


class GradeListView(ListView):
    model = Grade
    template_name = 'tracker/grade_list.html'
    context_object_name = 'grades'

class GradeCreateView(CreateView):
    model = Grade
    fields = '__all__'
    template_name = 'tracker/grade_form.html'
    success_url = reverse_lazy('grade-list')

class GradeUpdateView(UpdateView):
    model = Grade
    fields = '__all__'
    template_name = 'tracker/grade_form.html'
    success_url = reverse_lazy('grade-list')

class GradeDeleteView(DeleteView):
    model = Grade
    template_name = 'tracker/grade_confirm_delete.html'
    success_url = reverse_lazy('grade-list')


class SubjectListView(ListView):
    model = Subject
    template_name = 'tracker/subject_list.html'
    context_object_name = 'subjects'


class SubjectCreateView(CreateView):
    model = Subject
    fields = '__all__'
    template_name = 'tracker/subject_form.html'
    success_url = reverse_lazy('subject-list')

class SubjectUpdateView(UpdateView):
    model = Subject
    fields = '__all__'
    template_name = 'tracker/subject_form.html'
    success_url = reverse_lazy('subject-list')

class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'tracker/subject_confirm_delete.html'
    success_url = reverse_lazy('subject-list')

class TeacherListView(ListView):
    model = Teacher
    template_name = 'tracker/teacher_list.html'
    context_object_name = 'teachers'

class TeacherCreateView(CreateView):
    model = Teacher
    fields = '__all__'
    template_name = 'tracker/teacher_form.html'
    success_url = reverse_lazy('teacher-list')

class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = '__all__'
    template_name = 'tracker/teacher_form.html'
    success_url = reverse_lazy('teacher-list')

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'tracker/teacher_confirm_delete.html'
    success_url = reverse_lazy('teacher-list')





class MarkListView(ListView):
    model = Mark
    template_name = 'tracker/mark_list.html'
    context_object_name = 'marks'


class MarkCreateView(CreateView):
    model = Mark
    template_name = 'tracker/mark_form.html'
    fields = '__all__'
    success_url = reverse_lazy('mark-list')


class MarkUpdateView(UpdateView):
    model = Mark
    template_name = 'tracker/mark_form.html'
    fields = '__all__'
    success_url = reverse_lazy('mark-list')



class AttendaceListView(ListView):
    model = Attendace
    template_name = 'tracker/attendace_list.html'
    context_object_name = 'attendace'

class AttendaceCreateView(CreateView):
    model = Attendace
    template_name = 'tracker/attendance_form.html'
    fields = '__all__'
    success_url = reverse_lazy('attendace')


def attendace_report(request):
    students = Student.objects.all()
    report = []


    for student in students:
        total = Attendace.objects.filter(student = student).count()
        present = Attendace.objects.filter(student=student, status='present').count()
        absent = Attendace.objects.filter(student=student, status= 'absent').count()
        excused = Attendace.objects.filter(student=student, status= 'excused').count()
        late = Attendace.objects.filter(student=student, status= 'late').count()

        percentage = (present / total) * 100 if total > 0 else 0

        report.append({
            'student' : student,
            'total' : total,
            'present' : present,
            'absent' : absent,
            'excused' : excused,
            'late' : late,
            'percentage' : round(percentage, 2)
        })

    context = {
        'report' : report
    }


    return render(request, 'tracker/attendace_report.html', context)