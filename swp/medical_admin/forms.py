from django import forms
from dashboard.models import MedicalAnnouncements
from django.contrib.admin.widgets import AdminDateWidget

class MedicalAnnouncementForm(forms.ModelForm):
    class Meta:
        model = MedicalAnnouncements
        fields = '__all__'

class AddAnnouncementForm(forms.ModelForm):
    announcement_title=forms.CharField(label='Announcement Title',widget=forms.TextInput(attrs={"class":"form-control"}))
    announcement = forms.CharField(label='Announcement',widget=forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model = MedicalAnnouncements
        fields = ['announcement_title', 'announcement']
