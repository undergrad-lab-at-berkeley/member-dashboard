from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('', include('django.contrib.auth.urls')),
    path('announcement/<int:announcement_id>/', views.announcement, name='announcement'),
    path('announcement/<int:announcement_id>/edit', views.edit_announcement, name='edit_announcement'),
    path('announcement/all', views.all_announcements, name='all_announcements'),
    path('announcement/create', views.create_announcement, name='create_announcement'),
    path('people/<slug:username>/', views.profile, name='profile'),
    path('people/', views.people_directory, name='people'),
    path('projects/<int:proj_id>/', views.project, name='project'),
    path('projects/', views.projects_directory, name='projects'),
    path('projects/my_projects', views.user_projects, name='user_projects'),
    path('people/<slug:username>/edit', views.edit_profile, name='edit_profile'),
    path('groups/<int:group_id>/', views.group_page, name='group'),
    path('groups/<int:group_id>/settings', views.group_settings, name='group_settings'),
    path('groups/', views.user_groups, name='user_groups'),
]

#django.contrib.auth.urls includes registration views