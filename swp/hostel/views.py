from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .models import *
from .forms import *
from dashboard.models import HostelAnnouncements
from django.contrib.auth.decorators import login_required
from api_integration.models import Student
import datetime
from api_integration.models import Student
import os

@login_required
def get_admin_status(request):
	st = 0
	dr = Student.objects.filter(student_first_name = str(request.user))
	if(len(dr) == 0):
            return 0
	print(dr, "ASDAS")
	if(dr[0].is_hostel_admin == True):
		st = 1
	elif(dr[0].is_mess_admin == True):
		st = 2
	elif(dr[0].is_medical_admin == True):
		st = 3
	return st


# Create your views here.

@login_required
def hostel_dashboard(request):
	h_announce = HostelAnnouncements.objects.all().filter(isDeleted=0)
	scrollL_announce = len(h_announce)
	if scrollL_announce <= 3:
		scrollL_announce = '140px'
	else:
		scrollL_announce = str(3 * 70)+ 'px'

	self_help = SelfHelpGroup.objects.all().filter(isDeleted=0)
	scrollL_self = len(self_help)

	if scrollL_self <= 3:
		scrollL_self = '70px'
	else:
		scrollL_self = str(3 * 70)+ 'px'

	courier_data = Courrier.objects.all().filter(isDeleted=0)
	#.filter(student=Student.objects.get(user = request.user))
	courier_data = list(filter(lambda x: x.student.user == request.user, courier_data))
	scrollL_courier = len(courier_data)
	if scrollL_courier <= 3:
		scrollL_courier = '140px'
	else:
		scrollL_courier = str(3 * 70)+ 'px'
	context = {'h_announce':h_announce , 'self_help':self_help , 'courier_data':courier_data,
	'scrollL_announce':scrollL_announce,'scrollL_self':scrollL_self,'scrollL_courier':scrollL_courier,'admin_status': get_admin_status(request)}
	return render(request,'hostel/hostel_dashboard.html',context)

@login_required
def leave_form(request):
	form = HostelLeaveForm()
	return render(request,'hostel/leave.html',{'form':form,'admin_status': get_admin_status(request)})

@login_required
def complaint_form(request):
	form = HostelComplaintForm()
	return render(request,'hostel/complaint.html',{'form':form,'admin_status': get_admin_status(request)})

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
	if request.method == 'POST':
		form = HostelComplaintForm(request.POST,request.FILES)
		if form.is_valid():
			complaint_form = form.save(commit=False)
			complaint_form.student = Student.objects.get(user = request.user)
			subject = request.POST['subject']
			comp = subject +' '+request.POST['complaint']
			checkVal = vulgarCheck(comp)
			print(checkVal)
			if(checkVal==0):
				complaint_form.complaint = comp
			elif(checkVal==1):
				return render(request,'hostel/vulgar-ack.html',{'admin_status': get_admin_status(request)})

			if len(request.FILES) > 0:
				complaint_form.comp_img = request.FILES['image']
			else:
				complaint_form.comp_img = ""
			complaint_form.room_no = request.POST['room_no']
			complaint_form.completed = False
			complaint_form.timestamp = datetime.datetime.now()
			complaint_form.created_at = datetime.datetime.now().date()
			complaint_form.created_by = Student.objects.get(user = request.user)
			complaint_form.modified_at = datetime.datetime.now().date()
			complaint_form.modified_by = Student.objects.get(user = request.user)
			complaint_form.save()
			return render(request,'hostel/complaint-ack.html',{'admin_status': get_admin_status(request)})
	else:
		form =  HostelComplaintForm()
		return render(request,'hostel/complaint.html',{'form':form,'error_message':'','admin_status': get_admin_status(request)})




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
			return render(request, 'hostel/leave-ack.html',{'admin_status': get_admin_status(request)})
		else:
			error_message = "Please enter data in YYYY-MM-DD format"
			return render(request,'hostel/leave.html',{'form':form,'error_message':error_message,'admin_status': get_admin_status(request)})

	form =  HostelLeaveForm()
	return render(request,'hostel/leave.html',{'form':form,'error_message':'','admin_status': get_admin_status(request)})

def vulgarCheck(s):
	vul = dict()
	with open(os.getcwd()+"/vulgar.txt",'r') as file:
		text = file.readlines()
		for i in range(len(text)):
			text[i]=text[i].strip()
			if(text[i] not in vul):
				vul[text[i]] = 1

	s = s.split(' ')
	for j in range(len(s)):
		if(s[j] in vul):
			return 1

		if(j>0):
			if((s[j-1]+' '+s[j]) in vul):
				return 1

		if(j>1):
			if((s[j-2]+' '+s[j-1]+' '+s[j]) in vul):
				return 1

		if(j>2):
			if((s[j-3]+' '+s[j-2]+' '+s[j-1]+' '+s[j]) in vul):
				return 1

	return 0