from django.shortcuts import render
from api_integration.models import Student
from django.contrib.auth.models import User

def index(request):
    print(request.user)
    if(request.user.is_authenticated):
        if(Student.objects.get(user=request.user).is_medical_admin):
            return render(request, 'medical_admin/index.html')
        elif(Student.objects.get(user=request.user).is_mess_admin):
            return render(request, 'mess_admin/index.html')
        elif(Student.objects.get(user=request.user).is_hostel_admin):
            return render(request, 'hostel_admin/index.html')
    return render(request, 'index.html')
