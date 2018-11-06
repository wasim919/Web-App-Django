from django import forms
from dashboard.models import HostelAnnouncements
from django.contrib.admin.widgets import AdminDateWidget


class HostelAnnouncementForm(forms.ModelForm):
    class Meta:
        model = HostelAnnouncements
        fields = '__all__'

class HostelAnnouncements(forms.ModelForm):
    announcement_title=forms.CharField(label='announcement_title',widget=forms.TextInput(attrs={"class":"form-control"}))
    # announcement=forms.CharField(label='announcement',widget=forms.Textarea)
    announcement = forms.TextInput(attrs={'size': 10, 'title': 'announcement'})
    class Meta:
        model = HostelAnnouncements
        fields = ['announcement_title', 'announcement']
