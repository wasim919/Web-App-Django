from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from api_integration.models import Student

class EditUserNameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
        )

class EditBioAvatarForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'bio',
        )

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('avatar', )
