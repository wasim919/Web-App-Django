import os
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from api_integration.models import Student
from django.contrib.auth.models import User
from .forms import EditUserNameForm, EditBioAvatarForm
from django.http import JsonResponse
from django.views import View
from .forms import PhotoForm
from api_integration.models import Student
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




@login_required
def dashboard_index(request):
    # hostel_announcements = get_list_or_404(HostelAnnouncements, )
    hostel_announcements = list(HostelAnnouncements.objects.all().filter(isDeleted=0))
    hostel_announcements.sort(key = lambda a: a.timestamp, reverse = True)

    mess_announcements = list(MessAnnouncements.objects.all().filter(isDeleted=0))
    mess_announcements.sort(key = lambda a: a.timestamp, reverse = True)

    medical_announcements = list(MedicalAnnouncements.objects.all().filter(isDeleted=0))
    medical_announcements.sort(key = lambda a: a.timestamp, reverse = True)

    return render(request, 'dashboard/index.html', {
    'hostel_announcements': hostel_announcements,
    'mess_announcements': mess_announcements,
    'medical_announcements': medical_announcements,
    'admin_status': get_admin_status(request)
    })

@login_required
def announcement_detail(request, flag, pk):
    if flag == '1':
        announcement = get_object_or_404(HostelAnnouncements, pk = pk)
        return render(request, 'dashboard/announcement.html', {
        'announcement': announcement,
        'admin_status': get_admin_status(request)
        })
    elif flag == '2':
        announcement = get_object_or_404(MessAnnouncements, pk = pk)
        return render(request, 'dashboard/announcement.html', {
        'announcement': announcement,
        'admin_status': get_admin_status(request)
        })
    elif flag == '3':
        announcement = get_object_or_404(MedicalAnnouncements, pk = pk)
        return render(request, 'dashboard/announcement.html', {
        'announcement': announcement,
        'admin_status': get_admin_status(request)
        })

@login_required
def upload_image(request):
    a  = ""
    if len(request.FILES) > 0:
        if request.FILES['myfile']:
            student = get_object_or_404(Student, user = request.user)
            myfile = request.FILES['myfile']
            student.avatar = 'media/images/'+myfile.name
            a = student.bio
            student.save()
    return redirect('/dashboard/profile')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditUserNameForm(data = request.POST, instance=request.user)
        student = get_object_or_404(Student, user = request.user)
        bio_post = request.POST.get("editor")
        if bio_post != '' and student.bio != bio_post:
            student.bio = request.POST.get("editor")
            student.save()
        if form.is_valid():
            form.save()
        return redirect('/dashboard/profile')
    else:
        student = get_object_or_404(Student, user = request.user)
        form = EditUserNameForm(instance=request.user)
        try:
            messages = Messages.objects.all().filter(student = student)
        except Messages.DoesNotExist:
            messages = None
        print(messages)
        if messages is not None:
            return render(request, 'dashboard/edit_profile.html', {
                'form': form,
                'student': student,
                'bio': student.bio,
                'messages': messages
            })
        return render(request, 'dashboard/edit_profile.html', {
            'form': form,
            'student': student,
            'bio': student.bio,
            'messages': []
            'admin_status': get_admin_status(request)
        })

# @login_required
# class BasicUploadView(View):
#     def get(self, request):
#         student = get_object_or_404(Student, user = request.user)
#         return render(self.request, 'photos/basic_upload/index.html', {'avatar': student.avatar})
#
#     def post(self, request):
#         form = PhotoForm(self.request.POST, self.request.FILES)
#         if form.is_valid():
#             photo = form.save()
#             data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
#         else:
#             data = {'is_valid': False}
#         return JsonResponse(data)

@login_required
def contacts(request):
    imp_contacts = list(ImportantContacts.objects.all().filter(isDeleted=0))
    return render(request, 'dashboard/important_contacts.html', {
        'imp_contacts': imp_contacts,
        'admin_status': get_admin_status(request)
    })
