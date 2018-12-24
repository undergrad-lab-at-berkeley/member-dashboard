from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Announcement, Member, Project, Subgroup
from django.db.models import Value
from django.db.models.functions import Concat
from django.contrib.auth import authenticate, login
from .forms import CustomAuthForm as AuthenticationForm
from .forms import EditUserForm, EditMemberForm, CreateAnnouncementForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse


from datetime import datetime
import pdb

# DECORATORS
def check_login(func):
    def new_func(request, *args, **kwargs):
        result = handle_login(request)
        if result[0]:
          return result[1]
        else:
          return func(request, *args, **kwargs)
    return new_func


# VIEWS
@check_login
def homepage(request):
    mostRecent = Announcement.objects.all().order_by('-date_posted')[:3]
    context = {
      'announcments': mostRecent,
      'form': AuthenticationForm()
    }
    return render(request, 'dashboard/homepage.html', context)

@check_login
def announcement(request, announcement_id):
    try:
        announcement = Announcement.objects.get(pk=announcement_id)
    except Announcement.DoesNotExist:
        return HttpResponseRedirect(reverse('all_announcements'))

    user_is_author = False
    if not request.user.is_anonymous and request.user.member == announcement.author:
      user_is_author = True
    context = {
      'msg': announcement,
      'user_is_author': user_is_author,
      'form': AuthenticationForm()
    }
    return render(request, 'dashboard/announcement.html', context)

@check_login
def all_announcements(request):
    mostRecent = Announcement.objects.all().order_by('-date_posted')
    context = {
      'announcments': mostRecent,
      'form': AuthenticationForm()
    }
    return render(request, 'dashboard/all_announcements.html', context)

@check_login
def profile(request, username):
    auth_user = get_object_or_404(User, username=username)
    context = {
      'profile': auth_user.member,
      'form': AuthenticationForm()
    }
    return render(request, 'dashboard/profile.html', context)

@check_login
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
      'search_val': search_val,
      'form': AuthenticationForm()
    }
    return render(request, 'dashboard/people_directory.html', context)

@check_login
def project(request, proj_id):
    project = get_object_or_404(Project, pk=proj_id)
    context = {
      'project': project,
      'form': AuthenticationForm()
    }
    return render(request, 'dashboard/project.html', context)

@check_login
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

# @login_required
def edit_profile(request, username):
    auth_user = request.user
    profile = auth_user.member

    if auth_user.username != username or not auth_user.is_authenticated:
      return HttpResponseRedirect('/dashboard/people/')

    if request.method == 'POST':
      userForm = EditUserForm(request.POST, instance=auth_user, prefix="userForm")
      memberForm = EditMemberForm(request.POST, instance=profile, prefix="memberForm")
      if userForm.is_valid() and memberForm.is_valid():
        auth_user.save()
        profile.save()
        return HttpResponseRedirect(reverse('profile', kwargs={
          'username': auth_user.username
        }))

    else:
      userForm = EditUserForm(instance=auth_user, prefix="userForm")
      memberForm = EditMemberForm(instance=profile, prefix="memberForm")

    context = {
      'profile': profile,
      'userForm': userForm,
      'memberForm': memberForm,
      'form': AuthenticationForm()
    }
    return render(request, 'dashboard/edit_profile.html', context)

def create_announcement(request):
    user = request.user
    profile = user.member
    
    if not user.is_staff:
        return HttpResponseRedirect(reverse('all_announcements'))

    if request.method == 'POST':
      announcementForm = CreateAnnouncementForm(request.POST, prefix="announcementForm")
      if announcementForm.is_valid():
        newAnnouncement = announcementForm.save(commit=False)
        newAnnouncement.author = profile
        newAnnouncement.date_posted = datetime.now()
        newAnnouncement.save()
        return HttpResponseRedirect(reverse('announcement', kwargs={
          'announcement_id': newAnnouncement.id
          }))

    else:
      announcementForm = CreateAnnouncementForm(request.POST, prefix="announcementForm")

    context = {
      'profile': profile,
      'announcementForm': announcementForm,
      'form': AuthenticationForm()
    }
    return render(request, 'dashboard/create_announcement.html', context)

def edit_announcement(request, announcement_id):
    try:
        announcement = Announcement.objects.get(pk=announcement_id)
    except Announcement.DoesNotExist:
        return HttpResponseRedirect(reverse('all_announcements'))
    
    user = request.user
    profile = user.member
    
    if not user.is_staff or announcement.author != profile:
        return HttpResponseRedirect(reverse('announcement', kwargs={
          'announcement_id': announcement.id
        }))

    if request.method == 'POST':
      if 'delete-announcement' in request.POST.keys():
        announcement.delete()
        return HttpResponseRedirect(reverse('all_announcements'))
      else:
        announcementForm = CreateAnnouncementForm(request.POST, instance=announcement, prefix="announcementForm")
        if announcementForm.is_valid():
          announcementForm.save()
          return HttpResponseRedirect(reverse('announcement', kwargs={
            'announcement_id': announcement.id
            }))
    else:
      announcementForm = CreateAnnouncementForm(instance=announcement, prefix="announcementForm")

    context = {
      'profile': profile,
      'announcementForm': announcementForm,
      'form': AuthenticationForm()
    }
    return render(request, 'dashboard/edit_announcement.html', context)

@check_login
def group_page(request, group_id):
    group = get_object_or_404(Subgroup, pk=group_id)
    context = {
      'group': group,
      'form': AuthenticationForm()
    }
    return render(request, 'dashboard/subgroup.html', context)

def user_groups(request):
    auth_user = request.user
    if not auth_user.is_authenticated:
      return HttpResponseRedirect('/dashboard/')
    profile = auth_user.member

    context = {
      'profile': profile
    }
    return render(request, 'dashboard/user_subgroups.html', context)

def user_projects(request):
    auth_user = request.user
    if not auth_user.is_authenticated:
      return HttpResponseRedirect('/dashboard/')
    profile = auth_user.member

    context = {
      'profile': profile
    }
    return render(request, 'dashboard/user_projects.html', context)


# HELPERS
def handle_login(request):
    if request.method == 'POST':
      if 'username' in request.POST and 'password' in request.POST:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
          login(request, form.get_user())
          return (True, redirect(request.get_full_path()))
    return (False, None)