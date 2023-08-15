from . import views
from django.urls import path
app_name = 'teacher'
urlpatterns = [
    path('', views.teacher_dashboard, name='teacher_dashboard'),
]