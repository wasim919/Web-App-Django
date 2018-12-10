from django.shortcuts import render, redirect
from dashboard.models import MedicalAnnouncements
from .forms import MedicalAnnouncementForm, AddAnnouncementForm
from django.http import HttpResponse
import datetime
import time
from django.template.loader import render_to_string
from medical.models import MedicalLeave,MedicalAppointment
from api_integration.models import Student
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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


def check_isMedicalAdmin(request):
    return Student.objects.get(user=request.user).is_medical_admin

@login_required
def medical_admin_index(request):
    if(check_isMedicalAdmin(request)):
        return render(request, 'medical_admin/index.html')
    return render(request,'index.html')
def get_months_num(s):
    c=0
    for i in s:
        if(int(i.created_at.date().month)==int(datetime.datetime.now().date().month)):
            c+=1
    return c

@login_required
def medical_admin_dashboard(request):
    if(check_isMedicalAdmin(request)):
        medical_announcements = list(MedicalAnnouncements.objects.all())
        medical_leave = MedicalLeave.objects.all()
        medical_announcements.sort(key = lambda a: a.timestamp, reverse = True)
        medical_appointments = MedicalAppointment.objects.all()
        appointments_this_month=get_months_num(medical_leave)
        return render(request, 'medical_admin/medical_admin_dashboard.html', {
        'medical_announcements': medical_announcements,'medical_leave':medical_leave,
        'medical_appointments':medical_appointments,
        'admin_status': get_admin_status(request)
        })
    return render(request,'index.html')
@login_required
def medical_announcement_delete(request, id):
    if(check_isMedicalAdmin(request)):
        print(id)
        announcement = MedicalAnnouncements.objects.get(pk=id)
        announcement.delete()
        medical_announcements = MedicalAnnouncements.objects.all()

        return render(request, 'medical_admin/medical_admin_dashboard.html', {
        'medical_announcements': medical_announcements,
        'admin_status': get_admin_status(request)
        })
    return render(request,'index.html')
@login_required
def medical_announcement_edit(request, id):
    if(check_isMedicalAdmin(request)):
        medical_announcement = MedicalAnnouncements.objects.get(pk=id)
        medical_announcement_form = AddAnnouncementForm(initial = {
        'announcement_title': medical_announcement.announcement_title,
        'announcement': medical_announcement.announcement,
        'admin_status': get_admin_status(request)
        })
        print(medical_announcement_form)

        return render(request, 'medical_admin/edit_announcements.html', {
        'form': medical_announcement_form,
        'id': id,
        'admin_status': get_admin_status(request)
        })
    return render(request,'index.html')
@login_required
def medical_add_announcement(request):
    if(check_isMedicalAdmin(request)):
        if request.method == 'GET':
            add_announcement_form = AddAnnouncementForm()
            return HttpResponse(render_to_string('medical_admin/add.html',context={
            'add_announcement_form': add_announcement_form,
            'admin_status': get_admin_status(request)
            }))
    return render(request,'index.html')
@login_required
def medical_add_announcement_url(request):
    if(check_isMedicalAdmin(request)):
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

                return redirect('medical_admin:medical_admin_dashboard')
    return render(request,'index.html')
@login_required
def medical_save_edit_changes(request, id):
    if(check_isMedicalAdmin(request)):
        if request.method == 'POST':
            try:
                announcement = MedicalAnnouncements.objects.get(pk=id)
            except MedicalAnnouncements.DoesNotExist:
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
            return redirect('medical_admin:medical_admin_dashboard')
    return render(request,'index.html')
@login_required
def medical_leave_details(request,id):
    if(check_isMedicalAdmin(request)):
        try:
            medical_leave=MedicalLeave.objects.get(pk=id)
            return render(request,'medical_admin/leave_details.html',context={'medical_leave':medical_leave, 'admin_status': get_admin_status(request)})
        except:
            pass
        return redirect('medical_admin:medical_admin_dashboard')
    return render(request,'index.html')
