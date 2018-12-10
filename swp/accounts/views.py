from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
# from .forms import StudentLoginForm
from django.http import HttpResponse
# from .models import Student
from django.contrib.auth.decorators import login_required

def student_login(request):
    return render(request, 'accounts/login.html')

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'index.html')
