from django.shortcuts import render

from django.http import HttpResponse
from .models import Announcement


# Create your views here.
def homepage(request):
    context = {
      'message': 'hey haha',
      'announcments': Announcement.objects.all()
    }
    return render(request, 'dashboard/homepage.html', context)