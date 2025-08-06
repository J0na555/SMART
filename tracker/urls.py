from django.urls import path 
from .views import StudentListView, StudentCreateView, StudentDeleteView, StudentUpdateView, MarkCreateView, MarkListView, MarkUpdateView


urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),
    path('student/create', StudentCreateView.as_view(), name='student-create'),
    path('student/<int:pk>/delete', StudentDeleteView.as_view(), name='student-delete'),
    path('student/<int:pk>/update', StudentUpdateView.as_view(), name="student-update"),
    path('student/<int:pk>/mark-list', MarkListView.as_view(), name= 'mark-list'),
    path('student/<int:pk>/mark/add',MarkCreateView.as_view(), name = 'add-mark' ),
    path('student/<int:pk>/mark/edit', MarkUpdateView.as_view(), name= 'edit-mark'),

]
