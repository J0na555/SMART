from django.urls import path 
from .views import StudentListView, StudentCreateView, StudentDeleteView, StudentUpdateView


urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),
    path('student/create', StudentCreateView.as_view(), name='student-create'),
    path('student/<int:pk>/delete', StudentDeleteView.as_view(), name='student-delete'),
    path('student/<int:pk>/update', StudentUpdateView.as_view(), name="student-update"),
    
]
