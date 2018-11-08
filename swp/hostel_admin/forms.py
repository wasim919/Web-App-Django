from django import forms
from dashboard.models import HostelAnnouncements
from django.contrib.admin.widgets import AdminDateWidget
from orders.models import Items

class HostelAnnouncementForm(forms.ModelForm):
    class Meta:
        model = HostelAnnouncements
        fields = '__all__'

# class HostelAnnouncements(forms.ModelForm):
#     announcement_title=forms.CharField(label='announcement_title',widget=forms.TextInput(attrs={"class":"form-control"}))
#     # announcement=forms.CharField(label='announcement',widget=forms.Textarea)
#     announcement = forms.TextInput(attrs={'size': 10, 'title': 'announcement'})
#     class Meta:
#         model = HostelAnnouncements
#         fields = ['announcement_title', 'announcement']

class AddAnnouncementForm(forms.ModelForm):
    announcement_title=forms.CharField(label='Announcement Title',widget=forms.TextInput(attrs={"class":"form-control"}))
    announcement = forms.CharField(label='Announcement',widget=forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model = HostelAnnouncements
        fields = ['announcement_title', 'announcement']

class AddItemForm(forms.ModelForm):
    item_name=forms.CharField(label='Item Name',widget=forms.TextInput(attrs={"class":"form-control"}))
    # item_type = forms.CharField(label='Item Type',widget=forms.TextInput(attrs={"class":"form-control"}))
    cost=forms.FloatField(label='Cost',widget=forms.TextInput(attrs={"class":"form-control"}))
    quantity=forms.IntegerField(label='Quantity',widget=forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model = Items
        fields = ['item_name', 'cost', 'quantity']
