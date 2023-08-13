from . import views
from django.urls import path
app_name = 'student'
urlpatterns = [
    path('', views.student_dashboard, name='student_dashboard'),
]
