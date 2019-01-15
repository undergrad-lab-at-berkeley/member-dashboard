from django.shortcuts import render
from django.http import HttpResponse
from dashboard.forms import CustomAuthForm as AuthenticationForm
from dashboard.views import check_login

lab_content = {
			'cogsci': {
				'full_name': 'Psychology and Cognitive Sciences',
				'image': 'logos/logo_cog_sci.png'
			},
			'physics': {
				'full_name': 'Physics and Astronomy',
				'image': 'logos/logo_physics.png'
			},
			'bio': {
				'full_name': 'Genetic Engineering and Molecular Biology',
				'image': 'logos/logo_bio.png'
			},
			'health': {
				'full_name': 'Public Health',
				'image': 'logos/logo_public_health.png'
			},
			'data': {
				'full_name': 'Data Science',
				'image': 'logos/logo_data.png'
			},
			'atg': {
				'full_name': 'Advanced Technologies Group',
				'image': 'logos/logo_atg.png'
			},
			'ops': {
				'full_name': 'Operations and Publicity',
				'image': 'logos/logo_general.png'
			},
			'aerospace': {
				'full_name': 'Robotics and Aerospace Engineering',
				'image': 'logos/logo_robotics_aero.png'
			},
		}

# Create your views here.
@check_login
def frontpage(request):
    context = {
		'labs': lab_content,
     	'form': AuthenticationForm(),
    }
    return render(request, 'landing/frontpage.html', context)