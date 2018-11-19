from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('', include('django.contrib.auth.urls')),
    path('announcement/<int:announcement_id>/', views.announcement, name='announcement'),
    path('people/<slug:username>/', views.profile, name='profile'),
    path('people/', views.people_directory, name='people')
]

#django.contrib.auth.urls includes registration views