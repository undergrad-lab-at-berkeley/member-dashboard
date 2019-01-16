from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('lab/<slug:lab>/', views.lab, name='lab'),
    # path('', include('django.contrib.auth.urls')),
]