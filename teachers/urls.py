from . import views
from django.urls import path

app_name = 'teacher'

urlpatterns = [
    path('', views.teacher_dashboard, name='teacher_dashboard'),
    path('post_grade/', views.post_student_grade, name='post_grade'),
    path('post_reference_book/', views.post_reference_book, name='post_reference_book'),
    path('update_grade/<int:grade_id>/', views.update_grade, name='update_grade'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
]