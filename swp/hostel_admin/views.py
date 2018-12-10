from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from dashboard.models import HostelAnnouncements
from .forms import HostelAnnouncementForm, AddAnnouncementForm, AddCourrierForm, AddItemForm
from django.http import HttpResponse
import datetime
import time
from api_integration.models import Student
from django.template.loader import render_to_string
from orders.models import ManualOrder
from .forms import AddItemForm, AddCourrierForm
from api_integration.models import Student
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from hostel.models import HostelLeave, ComplaintRegister, Courrier
from dashboard.models import Messages
import pytz
from api_integration.models import Student


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


def check_isHostelAdmin(request):
	return Student.objects.get(user=request.user).is_hostel_admin

@login_required
def hostel_admin_index(request):
	if(check_isHostelAdmin(request)):
		return render(request, 'hostel_admin/index.html')
	return render(request,'index.html')

@login_required
def hostel_admin_dashboard(request):
	if(check_isHostelAdmin(request)):
		hostel_announcements = list(HostelAnnouncements.objects.all().filter(isDeleted = False))
		hostel_announcements.sort(key = lambda a: a.timestamp, reverse = True)

		return render(request, 'hostel_admin/hostel_admin_dashboard.html', {
		'hostel_announcements': hostel_announcements,
		'admin_status': get_admin_status(request)
		})
	return render(request,'index.html')

# announcement_title=forms.CharField(label='announcement_title',widget=forms.TextInput(attrs={"class":"form-control"}))
# announcement=forms.CharField(label='announcement',widget=forms.TextInput(attrs={"class":"form-control"}))
# timestamp=forms.DateField(label='timestamp',input_formats=['%Y-%m-%d'],widget=forms.DateInput(format = '%Y-%m-%d',attrs={"class":"form-control","id":"to_date","name":"date1","placeholder":"YYYY-MM-DD","type":"text"}))
# created_at=timestamp=forms.DateField(label='created_at',input_formats=['%Y-%m-%d'],widget=forms.DateInput(format = '%Y-%m-%d',attrs={"class":"form-control","id":"to_date","name":"date1","placeholder":"YYYY-MM-DD","type":"text"}))
# created_by=forms.CharField(label='created_by',widget=forms.TextInput(attrs={"class":"form-control"}))
# modified_at=timestamp=forms.DateField(label='modified_at',input_formats=['%Y-%m-%d'],widget=forms.DateInput(format = '%Y-%m-%d',attrs={"class":"form-control","id":"to_date","name":"date1","placeholder":"YYYY-MM-DD","type":"text"}))
# modified_by=forms.CharField(label='modified_by',widget=forms.TextInput(attrs={"class":"form-control"}))
@login_required
def announcement_delete(request, id):
	if(check_isHostelAdmin(request)):
		print(id)
		announcement = HostelAnnouncements.objects.get(pk=id)
		announcement.isDeleted = True
		hostel_announcements = HostelAnnouncements.objects.all()
		return render(request, 'hostel_admin/hostel_admin_dashboard.html', {
		'hostel_announcements': hostel_announcements,
		'admin_status': get_admin_status(request)
		})
	return render(request,'index.html')
@login_required
def announcement_edit(request, id):
	if(check_isHostelAdmin(request)):
		hostel_announcement = HostelAnnouncements.objects.get(pk=id)
		hostel_announcement_form = AddAnnouncementForm(initial = {
		'announcement_title': hostel_announcement.announcement_title,
		'announcement': hostel_announcement.announcement,
		'admin_status': get_admin_status(request)
		})
		print(hostel_announcement_form)
		return render(request, 'hostel_admin/edit_announcements.html', {
		'form': hostel_announcement_form,
		'id': id,
		'admin_status': get_admin_status(request)
		})
	return render(request,'index.html')

@login_required
def add_announcement(request):
	if(check_isHostelAdmin(request)):
		if request.method == 'GET':
			add_announcement_form = AddAnnouncementForm()
			return HttpResponse(render_to_string('hostel_admin/add.html',context={
			'add_announcement_form': add_announcement_form,
			'admin_status': get_admin_status(request)
			}))
	return render(request,'index.html')

@login_required
def add_announcement_url(request):
	if(check_isHostelAdmin(request)):
		if request.method == 'POST':
			form = AddAnnouncementForm(request.POST)
			if form.is_valid():
				add_announcement_form=form.save(commit=False)
				add_announcement_form.timestamp=datetime.datetime.now()
				add_announcement_form.created_at=datetime.datetime.now().date()
				add_announcement_form.modified_at = datetime.datetime.now().date()
				add_announcement_form.created_by=request.user.username
				add_announcement_form.modified_by=request.user.username
				add_announcement_form.save()

				return redirect('hostel_admin:hostel_admin_dashboard')
	return render(request,'index.html')

@login_required
def save_edit_changes(request, id):
	if(check_isHostelAdmin(request)):
		if request.method == 'POST':
			try:
				announcement = HostelAnnouncements.objects.get(pk=id)
			except HostelAnnouncements.DoesNotExist:
				announcement = None
			if announcement is not None:
				announcement_title = request.POST.get('announcement_title')
				announcement_body = request.POST.get('announcement')
				flag = 0
				if announcement_title != announcement.announcement_title:
					announcement.announcement_title = announcement_title
					flag = 1
					announcement.announcement = announcement_body
					announcement.timestamp=datetime.datetime.now()
					announcement.modified_at = datetime.datetime.now().date()
					announcement.modified_by=request.user.username
				if announcement_body != announcement.announcement:
					announcement.announcement = announcement_body
					if flag == 0:
						announcement.timestamp=datetime.datetime.now()
						announcement.modified_at = datetime.datetime.now().date()
						announcement.modified_by=request.user.username
				announcement.save()
			return redirect('hostel_admin:hostel_admin_dashboard')
	return render(request,'index.html')

@login_required
def manual_orders(request):
	if(check_isHostelAdmin(request)):
	  if request.method == 'GET':
		  manual_orders = ManualOrder.objects.all()
		  length = len(manual_orders)
		  return HttpResponse(render_to_string('hostel_admin/manual_order.html',context={
		  'manual_orders': manual_orders,
		  'len': length,
		  'admin_status': get_admin_status(request)	
		  }))
	  return render(request,'index.html')

@login_required
def add_item(request):
	if(check_isHostelAdmin(request)):
		if request.method == 'POST':
			add_item_form = AddItemForm(data = request.POST)
			if add_item_form.is_valid():
				form = add_item_form.save(commit = False)
				form.item_type = 'Others'
				form.timestamp=datetime.datetime.now()
				form.created_at = datetime.datetime.now().date()
				# print(form.created_at)
				# print('hi')
				form.modified_at = datetime.datetime.now().date()
				form.modified_by = request.user.username
				form.created_by = request.user.username
				print('hi')
				form.save()
				print('done')
			return redirect('hostel_admin:hostel_admin_dashboard')
		else:
			item_form = AddItemForm()
			return HttpResponse(render_to_string('hostel_admin/item_form.html',context={
			'form': item_form,
			'admin_status': get_admin_status(request)
			}))
			return render(request,'index.html')

def hostel_leaves(request):
	if request.method == 'GET':
		hostel_leaves = HostelLeave.objects.all().filter(isDeleted = False)
		print(hostel_leaves)
		length = len(hostel_leaves)
		return HttpResponse(render_to_string('hostel_admin/hostel_leave.html',context={
		'hostel_leaves': hostel_leaves,
		'len': length,
		}))

def hostel_leave_accept(request, id):
	error_message=""
	subject="Hostel Leave Accepted"
	student = Student.objects.get(user = request.user)
	# to_email='iiitsmedical@gmail.com'   #hardcoded to avoid any hacks
	to_email = student.student_email
	body="Your Hostel Leave has been accepted."
	message=render_to_string('hostel_admin/message.html',{'from':'iiitshostel@gmail.com','body':body})
	print(message)
	email=EmailMessage(subject,message,to=[to_email])
	email.send()
	leave = HostelLeave.objects.get(pk = id)
	leave.isDeleted = True
	leave.save()
	message = Messages.objects.create(student = student,
	message = message,
	created_at = datetime.datetime.now().date(),
	modified_at = datetime.datetime.now().date(),
	modified_by = request.user.username,
	created_by = request.user.username)
	message.save()

	return redirect('hostel_admin:hostel_admin_dashboard')

def hostel_leave_reject(request, id):
	error_message=""
	subject="Hostel Leave Rejected"
	student = Student.objects.get(user = request.user)
	# to_email='iiitsmedical@gmail.com'   #hardcoded to avoid any hacks
	to_email = student.student_email
	body="Your Hostel Leave can not be accepted."
	message=render_to_string('hostel_admin/message.html',{'from':'iiitshostel@gmail.com','body':body})
	email=EmailMessage(subject,message,to=[to_email])
	email.send()
	leave = HostelLeave.objects.get(pk = id)
	leave.isDeleted = True
	leave.save()
	message = Messages.objects.create()
	message.student = student
	message.message = message
	message.created_at = datetime.datetime.now().date()
	message.modified_at = datetime.datetime.now().date()
	message.modified_by = request.user.username
	message.created_by = request.user.username
	message.isDeleted = 0
	message.save()
	return redirect('hostel_admin:hostel_admin_dashboard')

def hostel_complaints(request):
	complaints = ComplaintRegister.objects.all()
	print(complaints)
	length = len(complaints)
	return HttpResponse(render_to_string('hostel_admin/complaints.html',context={
	'complaints': complaints,
	'len': length,
	'admin_status': get_admin_status(request)
	}))

def complaint_details(request, id):
	try:
		complaint = ComplaintRegister.objects.get(pk=id)
	except ComplaintRegister.DoesNotExist:
		complaint = None
	if complaint is not None:
		return render(request, 'hostel_admin/detail.html', {
		'complaint': complaint,
		'admin_status': get_admin_status(request)
		})
	else:
		return redirect('hostel_admin:hostel_admin_dashboard')

def add_courier(request):
	form = AddCourrierForm()
	return HttpResponse(render_to_string('hostel_admin/courrier_form.html',context={
	'courrier_form': form
	}))

def add_student_courrier(request):
	if request.method == 'POST':
		form = AddCourrierForm(request.POST,request.FILES)
		if form.is_valid():
			courrier_form = form.save(commit=False)
			student_roll = request.POST['student']
			courrier_form.courrier_ref_no = request.POST['courrier_ref_no']
			courrier_form.student = Student.objects.get(roll = student_roll)
			courrier_form.delivery_agent = request.POST['delivery_agent']
			courrier_form.courrier_company = request.POST['courrier_company']
			courrier_form.timestamp = datetime.datetime.now()
			courrier_form.expected_arrival_time = datetime.datetime.now().time()
			courrier_form.created_at = datetime.datetime.now().date()
			courrier_form.created_by = request.user.username
			courrier_form.modified_at = datetime.datetime.now().date()
			courrier_form.modified_by = request.user.username
			courrier_form.save()
			return render(request,'hostel_admin/courrier_form.html',{'admin_status': get_admin_status(request)})
	else:
		form =  AddCourrierForm()
		return render(request,'hostel_admin/courrier_form.html',{'form':form,'error_message':'','admin_status': get_admin_status(request)})

