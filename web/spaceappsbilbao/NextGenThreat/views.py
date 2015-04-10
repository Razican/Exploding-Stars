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
	context = {'name': 'Stephane'}
	return render(request, 'NextGenThreat/credits.html', context)
