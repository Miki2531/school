# accounts/views.py
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from .forms import LoginForm, LogoutForm
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("User role:", user.user_role)
                if user.user_role == 'admin':
                    print("User role:", user.user_role)
                    return redirect(reverse('admin_dash:admin_dash'))
                elif user.user_role == 'teacher':
                    return redirect(reverse('teacher:teacher_dashboard'))
                elif user.user_role == 'student':
                    return redirect(reverse('student:student_dashboard'))
            else:
                # Invalid credentials
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Redirect to login page
    else:
        form = LogoutForm()
    return render(request, 'logout.html', {'form': form})
