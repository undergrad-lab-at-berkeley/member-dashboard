from django.shortcuts import render
from django.http import HttpResponse, Http404
from dashboard.forms import CustomAuthForm as AuthenticationForm
from dashboard.views import check_login
from landing.lab_content import lab_content
from landing.member_content import member_content, founders, advisors, directors

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

    lab = lab_content[lab]
    staff = {name: member_content[name] for name in lab['staff']}
    context = {
		'labs': lab_content,
     	'lab': lab,
     	'staff': staff,
     	'form': AuthenticationForm()
    }
    return render(request, 'landing/lab.html', context)

@check_login
def about(request):
    context = {
        'labs': lab_content,
        'founders': {name: member_content[name] for name in founders},
        'advisors': {name: member_content[name] for name in advisors},
        'directors': {name: member_content[name] for name in directors},
        'form': AuthenticationForm(),
    }
    return render(request, 'landing/about.html', context)