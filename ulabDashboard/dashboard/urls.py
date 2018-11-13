from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('', include('django.contrib.auth.urls'))
]

#django.contrib.auth.urls includes registration views