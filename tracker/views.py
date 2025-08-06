# from django.shortcuts import render
# from urllib import request
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from .models import Student, Mark
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
    success_url = reverse_lazy('mark-list')



