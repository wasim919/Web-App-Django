from django.shortcuts import render, redirect
from dashboard.models import MedicalAnnouncements
from .forms import MedicalAnnouncementForm, AddAnnouncementForm
from django.http import HttpResponse
import datetime
import time
from django.template.loader import render_to_string

def medical_admin_index(request):
    return render(request, 'medical_admin/index.html')

def medical_admin_dashboard(request):
    medical_announcements = list(MedicalAnnouncements.objects.all())
    medical_announcements.sort(key = lambda a: a.timestamp, reverse = True)

    return render(request, 'medical_admin/medical_admin_dashboard.html', {
    'medical_announcements': medical_announcements,
    })

def medical_announcement_delete(request, id):
    print(id)
    announcement = MedicalAnnouncements.objects.get(pk=id)
    announcement.delete()
    medical_announcements = MedicalAnnouncements.objects.all()

    return render(request, 'medical_admin/medical_admin_dashboard.html', {
    'medical_announcements': medical_announcements,
    })

def medical_announcement_edit(request, id):
    medical_announcement = MedicalAnnouncements.objects.get(pk=id)
    medical_announcement_form = AddAnnouncementForm(initial = {
    'announcement_title': medical_announcement.announcement_title,
    'announcement': medical_announcement.announcement,
    })
    print(medical_announcement_form)

    return render(request, 'medical_admin/edit_announcements.html', {
    'form': medical_announcement_form,
    'id': id,
    })

def medical_add_announcement(request):
    if request.method == 'GET':
        add_announcement_form = AddAnnouncementForm()
        return HttpResponse(render_to_string('medical_admin/add.html',context={
        'add_announcement_form': add_announcement_form,
        }))

def medical_add_announcement_url(request):
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

def medical_save_edit_changes(request, id):
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
