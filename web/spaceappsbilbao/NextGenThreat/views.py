#-*-*- encoding: utf-8 -*-*-

from django.shortcuts import render
from django.template import RequestContext, loader, Context
from django.http import JsonResponse

from .models import Airburst

def index(request):
	return render(request, 'NextGenThreat/index.html', {})

def radar(request):
	latest_airburst_list = Airburst.objects.all()
	context = {'latest_airburst_list': latest_airburst_list}
	return render(request, 'NextGenThreat/radar.html', context)

def credits(request):
	context = {'contributors': [
			{'name': 'Aitor', 'lastname': 'Brazaola', 'description': 'Aitor is a student of Computer Engineering. Been a geek and software developer, he has a podcast with Iban Eguia named El Gato de Turing.'},
			{'name': 'Eneko', 'lastname': 'Cruz', 'description': 'Eneko is studying Computer Science at the University of Deusto and Mathematics at the National University of Distance Education (UNED). His main interests are information security, mathematics and computer vision.'},
			{'name': 'Elena', 'lastname': 'López de Dicastillo', 'description': 'Elena is a student at University of Deusto. She is studying Telecom Engineering and is very interested in fields such as Internet security, biomedicine and aeronautics. She is currently working on OpenStratos to send a Raspberry Pi to the stratosphere.'},
			{'name': 'Iban', 'lastname': 'Eguia', 'description': 'Iban is a future IT engineer and a total space geek. Translator and contributor at CodeIgniter and core developer at OpenStratos and XG Project. He has a podcast with Aitor Brazaola called El Gato de Turing.'},
			{'name': 'Alejandro', 'lastname': 'Pérez', 'description': 'Alejandro is a last year software engineering student, researcher in bioinformatics and net security and cofounder of aprenditeka.'},
		],
	}
	return render(request, 'NextGenThreat/credits.html', context)

def api(request):
	airburst_list = Airburst.objects.all()
	response = {}
	for airburst in airburst_list:
		response[airburst.id] = {'radiated_energy': airburst.radiated_energy,
								'impact_energy': airburst.impact_energy,
								'latitude': airburst.latitude,
								'longitude': airburst.longitude,
								'date': airburst.date.isoformat(),
								'altitude': airburst.altitude,
							}

	return JsonResponse(response)
