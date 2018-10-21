from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import HostelAnnouncements, MessAnnouncements, MedicalAnnouncements, ImportantContacts
from accounts.models import Student
from django.contrib.auth.models import User
from .forms import EditProfileForm

@login_required
def dashboard_index(request):
    hostel_announcements = get_list_or_404(HostelAnnouncements, )
    hostel_announcements.sort(key = lambda a: a.timestamp, reverse = True)

    mess_announcements = get_list_or_404(MessAnnouncements, )
    mess_announcements.sort(key = lambda a: a.timestamp, reverse = True)

    medical_announcements = get_list_or_404(MedicalAnnouncements, )
    medical_announcements.sort(key = lambda a: a.timestamp, reverse = True)

    return render(request, 'dashboard/index.html', {
    'hostel_announcements': hostel_announcements,
    'mess_announcements': mess_announcements,
    'medical_announcements': medical_announcements
    })

@login_required
def announcement_detail(request, flag, pk):
    if flag == '1':
        announcement = get_object_or_404(HostelAnnouncements, pk = pk)
        return render(request, 'dashboard/announcement.html', {
        'announcement': announcement
        })
    elif flag == '2':
        announcement = get_object_or_404(MessAnnouncements, pk = pk)
        return render(request, 'dashboard/announcement.html', {
        'announcement': announcement
        })
    elif flag == '3':
        announcement = get_object_or_404(MedicalAnnouncements, pk = pk)
        return render(request, 'dashboard/announcement.html', {
        'announcement': announcement
        })

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(data = request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/dashboard/profile')
    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'dashboard/edit_profile.html', {
            'form': form
        })

@login_required
def contacts(request):
    imp_contacts = get_list_or_404(ImportantContacts, )
    return render(request, 'dashboard/important_contacts.html', {
        'imp_contacts': imp_contacts
    })
