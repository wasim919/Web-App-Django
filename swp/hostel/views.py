from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from accounts.models import Student
import datetime

# Create your views here.

@login_required
def hostel_dashboard(request):
	return render(request,'hostel/hostel_dashboard.html')

@login_required
def leave_form(request):
	form = HostelLeaveForm()
	return render(request,'hostel/leave.html',{'form':form})

@login_required
def leave_ack(request):
	return render(request,'hostel/leave_ack.html')

@login_required
def complaint_form(request):
	return render(request,'hostel/complaint.html')

@login_required
def complaint_ack(request):
	return render(request,'hostel/complaint-ack.html')

