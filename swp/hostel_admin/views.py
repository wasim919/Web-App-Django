from django.shortcuts import render, redirect
from dashboard.models import HostelAnnouncements
from .forms import HostelAnnouncementForm

def hostel_admin_index(request):
    return render(request, 'hostel_admin/index.html')

def hostel_admin_dashboard(request):
    hostel_announcements = list(HostelAnnouncements.objects.all())
    hostel_announcements.sort(key = lambda a: a.timestamp, reverse = True)

    return render(request, 'hostel_admin/hostel_admin_dashboard.html', {
    'hostel_announcements': hostel_announcements,
    })

# announcement_title=forms.CharField(label='announcement_title',widget=forms.TextInput(attrs={"class":"form-control"}))
# announcement=forms.CharField(label='announcement',widget=forms.TextInput(attrs={"class":"form-control"}))
# timestamp=forms.DateField(label='timestamp',input_formats=['%Y-%m-%d'],widget=forms.DateInput(format = '%Y-%m-%d',attrs={"class":"form-control","id":"to_date","name":"date1","placeholder":"YYYY-MM-DD","type":"text"}))
# created_at=timestamp=forms.DateField(label='created_at',input_formats=['%Y-%m-%d'],widget=forms.DateInput(format = '%Y-%m-%d',attrs={"class":"form-control","id":"to_date","name":"date1","placeholder":"YYYY-MM-DD","type":"text"}))
# created_by=forms.CharField(label='created_by',widget=forms.TextInput(attrs={"class":"form-control"}))
# modified_at=timestamp=forms.DateField(label='modified_at',input_formats=['%Y-%m-%d'],widget=forms.DateInput(format = '%Y-%m-%d',attrs={"class":"form-control","id":"to_date","name":"date1","placeholder":"YYYY-MM-DD","type":"text"}))
# modified_by=forms.CharField(label='modified_by',widget=forms.TextInput(attrs={"class":"form-control"}))
def announcement_delete(request, id):
    print(id)
    announcement = HostelAnnouncements.objects.get(pk=id)
    announcement.delete()
    hostel_announcements = HostelAnnouncements.objects.all()
    return render(request, 'hostel_admin/hostel_admin_dashboard.html', {
    'hostel_announcements': hostel_announcements,
    })

def announcement_edit(request, id):
    # print(id)
    hostel_announcement = HostelAnnouncements.objects.get(pk=id)
    # print(hostel_announcement)
    hostel_announcement_form = HostelAnnouncementForm(initial = {
    'announcement_title': hostel_announcement.announcement_title,
    'announcement': hostel_announcement.announcement,

    })
    return render(request, 'hostel_admin/edit_announcements.html', {
    'form': hostel_announcement_form
    })
