from django.shortcuts import render
from django.http import HttpResponse, Http404
from dashboard.forms import CustomAuthForm as AuthenticationForm
from dashboard.views import check_login
from landing.lab_content import lab_content

# Create your views here.
@check_login
def frontpage(request):
    context = {
		'labs': lab_content,
     	'form': AuthenticationForm(),
    }
    return render(request, 'landing/frontpage.html', context)

@check_login
def lab(request, lab):
    if lab not in lab_content.keys():
    	raise Http404(lab)
    context = {
		'labs': lab_content,
     	'lab': lab_content[lab],
     	'form': AuthenticationForm()
    }
    return render(request, 'landing/lab.html', context)