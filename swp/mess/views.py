from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .models import *
from dashboard.models import MessAnnouncements
from django.contrib.auth.decorators import login_required
from accounts.models import Student
from .models import OrderListMess, OrderHistoryMess
import datetime

# Create your views here.

@login_required
def mess_dashboard(request):
	m_announce = MessAnnouncements.objects.all()
	o_list = OrderListMess.objects.all()
	o_hist = OrderHistoryMess.objects.all()
	o_list = list(filter(lambda x: x.student.user == request.user, o_list))
	h_list = list(filter(lambda x: x.student.user == request.user, o_hist))
	context = {'m_announce': m_announce, 'o_list': o_list, 'o_hist': o_hist}
	return render(request,'mess/home.html',context)

@login_required
def applyMessLeave(request):
	if request.method == 'POST':
		form = MessLeaveForm(request.POST)
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

			if(leave_form.leave_from >=  leave_form.leave_to):
				error_message = "Please enter valid From and TO dates"
				return render(request,'mess/leave.html',{'form':form,'error_message':error_message})
			leave_form.save()
			return render(request, 'mess/leave-ack.html')
		else:
			error_message = "Please enter data in YYYY-MM-DD format"
			return render(request,'mess/leave.html',{'form':form,'error_message':error_message})

	form =  MessLeaveForm()
	return render(request,'mess/leave.html',{'form':form,'error_message':''})

@login_required
def leave_form(request):
	#Add appropriate data to be passed to page
	return render(request,'mess/leave.html')

@login_required
def leave_ack(request):
	return render(request, 'mess/leave-ack.html')

@login_required
def refund_form(request):
	#Add appropriate data to be passed to page
	return render(request,'mess/refund.html')

@login_required
def refund_ack(request):
	return render(request, 'mess/refund-ack.html')

@login_required
def feedback_form(request):
	return render(request, 'mess/feedback.html')

@login_required
def feedback_ack(request):
	return render(request, 'mess/feedback-ack.html')

@login_required
def submit_feedback(request):
	if request.method == 'POST':
		form = feedback_form(request.POST)
		feedback_form = form.save(commit=False)
		refund_form.student = Student.objects.get(user = request.user)
		feedback_form.feedback = request.POST['feedback']
		feedback_form.timestamp = datetime.datetime.now()
		feedback_form.created_at = datetime.datetime.now().date()
		feedback_form.modified_at = datetime.datetime.now().date()
		
		feedback_form.created_by = Student.objects.get(user = request.user)
		feedback_form.modified_by = Student.objects.get(user = request.user)
		feedback_form.save()
		return render(request, 'mess/feedback-ack.html')

	form =  MessRefundForm()
	return render(request,'mess/feedback.html')

@login_required
def applyMessRefund(request):
	if request.method == 'POST':
		form = MessLeaveForm(request.POST)
		refund_form = form.save(commit=False)
		refund_form.student = Student.objects.get(user = request.user)
		refund_form.ref_amount = request.POST['ref_amount']
		refund_form.timestamp = datetime.datetime.now()
		refund_form.created_at = datetime.datetime.now().date()
		refund_form.modified_at = datetime.datetime.now().date()
		
		refund_form.created_by = Student.objects.get(user = request.user)
		refund_form.modified_by = Student.objects.get(user = request.user)
		refund_form.save()
		return render(request, 'mess/refund-ack.html')

	form =  MessRefundForm()
	return render(request,'mess/refund.html',{'form':form,'error_message':''})










