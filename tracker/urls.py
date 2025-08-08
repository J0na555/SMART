from django.urls import path 
from .views import StudentListView, StudentCreateView, StudentDeleteView, StudentUpdateView, MarkCreateView, MarkListView, MarkUpdateView, AttendaceListView, AttendaceCreateView, attendace_report, GradeCreateView, GradeListView, GradeUpdateView, GradeDeleteView, SubjectCreateView, SubjectListView, SubjectUpdateView, SubjectDeleteView, TeacherListView, TeacherCreateView, TeacherUpdateView, TeacherDeleteView


urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),
    path('student/create', StudentCreateView.as_view(), name='student-create'),
    path('student/<int:pk>/delete', StudentDeleteView.as_view(), name='student-delete'),
    path('student/<int:pk>/update', StudentUpdateView.as_view(), name="student-update"),
    path('marks/', MarkListView.as_view(), name='mark-list'),
    path('student/<int:pk>/mark-list', MarkListView.as_view(), name='student-mark-list'),
    path('student/<int:pk>/mark/add',MarkCreateView.as_view(), name = 'add-mark'),
    path('student/<int:pk>/mark/edit', MarkUpdateView.as_view(), name= 'edit-mark'),
    path('attendace/', AttendaceListView.as_view(), name= 'attendace'),
    path('attendace/add', AttendaceCreateView.as_view(), name='edit-attendace'),
    path('attendace/report', attendace_report, name= 'attendece-report'), 
    path('grade/', GradeListView.as_view(), name='grade-list'),
    path('grade/create', GradeCreateView.as_view(), name='grade-create'),
    path('grade/<int:pk>/update', GradeUpdateView.as_view(), name='grade-update'),
    path('grade/<int:pk>/delete', GradeDeleteView.as_view(), name='grade-delete'),
    path('subjects/', SubjectListView.as_view(), name='subject-list'),
    path('subjects/create', SubjectCreateView.as_view(), name='subject-create'),
    path('subjects/<int:pk>/update', SubjectUpdateView.as_view(), name='subject-update'),
    path('subjects/<int:pk>/delete', SubjectDeleteView.as_view(), name='subject-delete'),
    path('teachers/', TeacherListView.as_view(), name='teacher-list'), 
    path('teacher/create', TeacherCreateView.as_view(), name='teacher-create'),
    path('teacher/<int:pk>/update', TeacherUpdateView.as_view(), name='teacher-update'),
    path('teacher/<int:pk>/delete', TeacherDeleteView.as_view(), name='teacher-delete'), 
]