from django.shortcuts import render
from accounts.decorators import teacher_required
# Create your views here.
@teacher_required
def teacher_dashboard(request):
    teacher = request.user  # Assuming the logged-in user is a student
    context = {
        'teacher': teacher,
    }
    return render(request, 'teacher_dashboard.html', context)