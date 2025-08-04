from django.urls import path 
from .views import StudentListView, StudentCreateView, StudentDeleteView, StudentUpdateView


urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),
    path('student/create', StudentCreateView.as_view(), name='student-create'),
    path('stuent/<int:student_id>/delete', StudentDeleteView.as_view(), name='student-delete'),
    path('student/<int:student_id>/update', StudentUpdateView.as_view(), name="student-update"),
    
]
