from django import forms
from .models import HostelLeave
from .models import	ComplaintRegister

#Create Complaint Form as well

class HostelLeaveForm(forms.ModelForm):
	leave_from=forms.DateField(label='leave_from',input_formats=['%Y-%m-%d'],widget=forms.DateInput(format = '%Y-%m-%d',attrs={"class":"form-control","id":"from_date","name":"date","placeholder":"YYYY-MM-DD","type":"text"}))
	leave_to=forms.DateField(label='leave_to',input_formats=['%Y-%m-%d'],widget=forms.DateInput(format = '%Y-%m-%d',attrs={"class":"form-control","id":"to_date","name":"date1","placeholder":"YYYY-MM-DD","type":"text"}))
	hometown=forms.CharField(label='hometown',widget=forms.TextInput(attrs={"class":"form-control"}))
	reason=forms.CharField(label='reason',widget=forms.Textarea(attrs={"class":"form-control","rows":"4","cols":"50"}))
	class Meta:
		model = HostelLeave
		fields = ['leave_from','leave_to','hometown','reason']
