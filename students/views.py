from django.shortcuts import render
from accounts.decorators import student_required
# Create your views here.
@student_required
def student_dashboard(request):
    return render(request, 'students/student_dashboard.html')
