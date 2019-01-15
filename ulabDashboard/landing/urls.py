from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    # path('', include('django.contrib.auth.urls')),
]