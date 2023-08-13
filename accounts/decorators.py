# accounts/decorators.py
from functools import wraps
from django.shortcuts import redirect
from .models import CustomUser

def role_required(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user = request.user
            if user.is_authenticated and user.user_role in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('login')  # Redirect to login if not allowed
        return _wrapped_view
    return decorator

def admin_required(view_func):
    return role_required(allowed_roles=['admin'])(view_func)

def teacher_required(view_func):
    return role_required(allowed_roles=['admin', 'teacher'])(view_func)

def student_required(view_func):
    return role_required(allowed_roles=['admin', 'student'])(view_func)
