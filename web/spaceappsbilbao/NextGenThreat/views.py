#-*-*- encoding: utf-8 -*-*-

from django.shortcuts import render
from django.template import RequestContext, loader, Context

from .models import Airburst

def index(request):
	context = {'name': 'Stephane'}
	return render(request, 'NextGenThreat/index.html', context)

def radar(request):
	latest_airburst_list = Airburst.objects.all()
	context = {'latest_airburst_list': latest_airburst_list}
	return render(request, 'NextGenThreat/radar.html', context)

def credits(request):
	context = {'contributors': [
			{'name': 'Aitor', 'lastname': 'Brazaola', 'description': 'Aitor Brazaola nulla non metus auctor fringilla. Vestibulum id ligula porta felis euismod semper. Praesent commodo cursus magna, vel scelerisque nisl consectetur. Fusce dapibus, tellus ac cursus commodo.'},
			{'name': 'Elena', 'lastname': 'López', 'description': 'Elena López nulla non metus auctor fringilla. Vestibulum id ligula porta felis euismod semper. Praesent commodo cursus magna, vel scelerisque nisl consectetur. Fusce dapibus, tellus ac cursus commodo.'},
			{'name': 'Iban', 'lastname': 'Eguia', 'description': 'Iban Eguia nulla non metus auctor fringilla. Vestibulum id ligula porta felis euismod semper. Praesent commodo cursus magna, vel scelerisque nisl consectetur. Fusce dapibus, tellus ac cursus commodo.'},
			{'name': 'Eneko', 'lastname': 'Cruz', 'description': 'Eneko Cruz nulla non metus auctor fringilla. Vestibulum id ligula porta felis euismod semper. Praesent commodo cursus magna, vel scelerisque nisl consectetur. Fusce dapibus, tellus ac cursus commodo.'},
		],
	}
	return render(request, 'NextGenThreat/credits.html', context)
