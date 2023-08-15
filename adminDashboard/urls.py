from . import views
from django.urls import path
from .views import family_registration_view, student_registration_view
app_name = 'admin_dash'
urlpatterns = [
    path('', views.admin_dash, name='admin_dash'),
    path('register/', views.register_user, name='register'),
    path('register/family/', family_registration_view, name='family_registration'),
    path('register/student/', student_registration_view, name='student_registration'),
 
]

