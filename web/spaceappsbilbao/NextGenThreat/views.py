from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Airburst

# Create your views here.
def index(request):
	return HttpResponse("Hello world!")
def about(request):
	return HttpResponse("This is the about page")
def radar(request):
	latest_airburst_list = Airburst.objects.all()
	template = loader.get_template('NextGenThreat/radar.html')
	context = RequestContext(request, {
		'latest_airburst_list': latest_airburst_list,
	})
	return HttpResponse(template.render(context))