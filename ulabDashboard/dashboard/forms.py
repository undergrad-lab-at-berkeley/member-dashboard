from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.forms import ModelForm
from .models import Announcement, Member, Project
from django.conf import settings
AUTH_USER_MODEL = settings.AUTH_USER_MODEL

class CustomAuthForm(AuthenticationForm):
  username = forms.CharField(
    widget = TextInput(attrs = {
        'class': 'validate',
        'placeholder': 'Username'
    }))
  password = forms.CharField(
    widget = PasswordInput(attrs = {
        'placeholder': 'Password'
    }))


class EditMemberForm(ModelForm):
	class Meta:
		model = Member
		fields = ["bio", "linkedin", "github", "website"]