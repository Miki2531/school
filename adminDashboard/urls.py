from . import views
from django.urls import path


app_name = 'admin_dash'
urlpatterns = [
    path('', views.admin_dash, name='admin_dash'),
    path('register/', views.register_user, name='register'),
    path('create_student/', views.create_student, name='create_student'),
    path('create_employee/', views.create_employee, name='create_employee'),
    path('create_school_year/', views.SchoolYear, name='school_year'),
]

