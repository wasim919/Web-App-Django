from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .forms import MedicalLeaveForm
from .models import *
from django.contrib.auth.decorators import login_required
from accounts.models import Student
import datetime
# Create your views here.
@login_required
def medical_dashboard(request):
    return render(request,'medical/medical_dashboard.html')
@login_required
def medical_message(request):
    return render(request,'medical/medical_message.html')
@login_required
def medical_leave(request):
    form=MedicalLeaveForm()
    return render(request,'medical/medical_leave.html',{'form':form})
@login_required
def sendMessage(request):
    error_message=""
    if request.method == 'POST':
        subject=request.POST['subject']
        to_email='iiitsmedical@gmail.com'   #hardcoded to avoid any hacks
        body=request.POST['body']
        if(len(subject)==0):
            error_message="Subject can't be empty"
            if(len(body)==0):
                error_message="Subject and Message can't be empty"
            return render(request,'medical/medical_message.html',{"error_message":error_message})
        elif(len(body)==0):
            error_message="Message can't be empty"
            return render(request,'medical/medical_message.html',{"error_message":error_message})
        message=render_to_string('medical/message.html',{'from':request.user.username,'body':body})
        email=EmailMessage(subject,message,to=[to_email])
        email.send()
        return render(request,'medical/success.html')
    return render(request,'medical/medical_message.html',{"error_message":error_message})
def getDate(s):
    s=s.split('-')
    year=int(s[0])
    month=int(s[1])
    day=int(s[2])
    return datetime.date(year,month,day)
@login_required
def applyLeave(request):
    if request.method == 'POST':
        form = MedicalLeaveForm(request.POST)
        if form.is_valid():
            leave_form=form.save(commit=False)
            leave_form.student=Student.objects.get(user=request.user)
            leave_form.leave_from=getDate(request.POST['leave_from'])
            leave_form.leave_to=getDate(request.POST['leave_to'])
            if(leave_form.leave_from>=leave_form.leave_to):
                error_message="Please enter valid From and To dates"
                return render(request, 'medical/medical_leave.html', {
                'form': form,
                'error_message':error_message
                })
            leave_form.save()
            return render(request, 'medical/success.html')
        else:
            error_message="Please enter date in YYYY-MM-DD format"
            return render(request, 'medical/medical_leave.html', {
            'form': form,
            'error_message':error_message
            })
    form = MedicalLeaveForm()
    return render(request, 'medical/medical_leave.html', {
    'form': form,
    'error_message':''
    })
