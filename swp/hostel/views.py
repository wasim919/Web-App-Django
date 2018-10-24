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
def complaint_form(request):
	form = HostelComplaintForm()
	return render(request,'hostel/complaint.html',{'form':form})

'''@login_required
def complaint_ack(request):
	return render(request,'hostel/complaint-ack.html')'''

def getDate(dat):
	dat = dat.split('-')
	year = int(dat[0])
	month = int(dat[1])
	day = int(dat[2])

	return datetime.date(year,month,day)

@login_required
def addComplaint(request):
	return render(request,'hostel/complaint-ack.html')

@login_required
def applyHostelLeave(request):
	if request.method == 'POST':
		form = HostelLeaveForm(request.POST)
		if form.is_valid():
			leave_form = form.save(commit=False)
			leave_form.student = Student.objects.get(user = request.user)
			leave_form.leave_from = getDate(request.POST['leave_from'])
			leave_form.leave_to = getDate(request.POST['leave_to'])
			leave_form.timestamp = datetime.datetime.now()
			leave_form.created_at = datetime.datetime.now().date()
			leave_form.modified_at = datetime.datetime.now().date()
			
			leave_form.created_by = Student.objects.get(user = request.user)
			leave_form.modified_by = Student.objects.get(user = request.user)

			mess_leave = request.POST['select_opt']
#--------------------------------------------------------------------------------------------
			if(mess_leave=='Yes'):
				#Update the mess models with creating an instance of the mess models
				print(mess_leave)
#--------------------------------------------------------------------------------------------
			if(leave_form.leave_from >=  leave_form.leave_to):
				error_message = "Please enter valid From and TO dates"
				return render(request,'hostel/leave.html',{'form':form,'error_message':error_message})
			leave_form.save()
			return render(request, 'hostel/leave-ack.html')
		else:
			error_message = "Please enter data in YYYY-MM-DD format"
			return render(request,'hostel/leave.html',{'form':form,'error_message':error_message})

	form =  HostelLeaveForm()
	return render(request,'hostel/leave.html',{'form':form,'error_message':''})
