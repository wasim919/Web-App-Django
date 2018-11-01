from django import forms
from dashboard.models import HostelAnnouncements
from django.contrib.admin.widgets import AdminDateWidget


class HostelAnnouncementForm(forms.ModelForm):
    class Meta:
        model = HostelAnnouncements
        fields = '__all__'

class HostelAnnouncements(forms.ModelForm):
    announcement_title=forms.CharField(label='announcement_title',widget=forms.TextInput(attrs={"class":"form-control"}))
    announcement=forms.CharField(label='announcement',widget=forms.Textarea)
    # timestamp=forms.DateField(label='timestamp', widget=AdminDateWidget())
    # created_at=timestamp=forms.DateField(label='created_at',input_formats=['%Y-%m-%d'],widget=AdminDateWidget())
    # created_by=forms.CharField(label='created_by',widget=forms.TextInput(attrs={"class":"form-control"}))
    # modified_at=timestamp=forms.DateField(label='modified_at',input_formats=['%Y-%m-%d'],widget=forms.DateInput(format = '%Y-%m-%d',attrs={"class":"form-control","id":"to_date","name":"date1","placeholder":"YYYY-MM-DD","type":"text"}))
    # modified_by=forms.CharField(label='modified_by',widget=forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model = HostelAnnouncements
        fields = ['announcement_title', 'announcement']
