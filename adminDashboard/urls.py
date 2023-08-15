from . import views
from django.urls import path
app_name = 'admin_dash'
urlpatterns = [
    path('', views.admin_dash, name='admin_dash'),
    path('register/', views.register_user, name='register'),
    path('create_student/', views.create_student, name='create_student'),
]
