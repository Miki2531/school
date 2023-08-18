from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('accounts.urls')),
    path('admin_dash/', include('adminDashboard.urls')),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
]

"""Add the following line to serve media files during development"""
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
