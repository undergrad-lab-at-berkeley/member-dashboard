from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.forms import ModelForm
from .models import Announcement, Member, Project
from django.contrib.auth import get_user_model


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
		fields = ["active", "about", "linkedin", "github", "website"]

class EditUserForm(ModelForm):
	class Meta:
		model = get_user_model()
		fields = ["email"]
		help_texts = {
      'email': None
		}

class CreateAnnouncementForm(ModelForm):
  class Meta:
    model = Announcement
    fields = ["title", "description"]
    help_texts = {
      "title": None,
      "description": None
    }