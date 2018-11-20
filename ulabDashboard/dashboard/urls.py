from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('', include('django.contrib.auth.urls')),
    path('announcement/<int:announcement_id>/', views.announcement, name='announcement'),
    path('people/<slug:username>/', views.profile, name='profile'),
    path('people/', views.people_directory, name='people'),
    path('projects/<int:proj_id>/', views.project, name='project'),
    path('projects/', views.projects_directory, name='projects')
]

#django.contrib.auth.urls includes registration views