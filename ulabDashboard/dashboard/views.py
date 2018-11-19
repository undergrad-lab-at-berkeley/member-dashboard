from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Announcement, Member
from django.contrib.auth.forms import AuthenticationForm
# form = AuthenticationForm()


# Create your views here.
def homepage(request):
    context = {
      'announcments': Announcement.objects.all(),
      'form': AuthenticationForm()
    }
    return render(request, 'dashboard/homepage.html', context)

def announcement(request, announcement_id):
    announcement = get_object_or_404(Announcement, pk=announcement_id)
    context = {
      'msg': announcement,
      'form': AuthenticationForm()
    }
    return render(request, 'dashboard/announcement.html', context)

def profile(request, username):
    auth_user = get_object_or_404(User, username=username)
    context = {
      'profile': auth_user.member,
      'form': AuthenticationForm()

    }
    return render(request, 'dashboard/profile.html', context)

def people_directory(request):
    context = {
      'people': Member.objects.all(),
      'form': AuthenticationForm()
    }
    return render(request, 'dashboard/people_directory.html', context)