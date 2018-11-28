from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Announcement, Member, Project
from django.db.models import Value
from django.db.models.functions import Concat
from django.contrib.auth import authenticate, login
from .forms import CustomAuthForm as AuthenticationForm
from django.shortcuts import redirect

import pdb

# DECORATORS
def check_login(func):
    def new_func(request):
        result = handle_login(request)
        if result[0]:
          return result[1]
        else:
          return func(request)
    return new_func


# VIEWS
@check_login
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
    search_val = request.GET.get('search', '')

    # Filter with Full Name
    users = User.objects.annotate(
      full_name=Concat('first_name', Value(' '), 'last_name'),
    ).filter(full_name__icontains=search_val)
    member_ids = users.values_list('member', flat=True)
    people = Member.objects.filter(id__in=member_ids)

    context = {
      'people': people,
      'form': AuthenticationForm()
    }
    return render(request, 'dashboard/people_directory.html', context)

def project(request, proj_id):
    project = get_object_or_404(Project, pk=proj_id)
    context = {
      'project': project,
      'form': AuthenticationForm()
    }
    return render(request, 'dashboard/project.html', context)

def projects_directory(request):
    search_val = request.GET.get('search', '')

    projects_by_name = Project.objects.filter(name__icontains=search_val)
    projects_by_desc = Project.objects.filter(description__icontains=search_val)
    projects = (projects_by_name | projects_by_desc).distinct()

    context = {
      'projects': projects,
      'form': AuthenticationForm()
    }
    return render(request, 'dashboard/projects_directory.html', context)



# HELPERS
def handle_login(request):
    if request.method == 'POST':
      if 'username' in request.POST and 'password' in request.POST:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
          login(request, form.get_user())
          return (True, redirect(request.get_full_path()))
    return (False, None)