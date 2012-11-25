# Create your views here.

from models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


def alumnos_seccion(request, seccion):
	
	alumnos = Alumno.objects.filter(seccion_id=int(seccion)).order_by('nombre')

	return render_to_response('consulta_seccion.html', 
		{'alumnos': alumnos, 'seccion': seccion},
		context_instance=RequestContext(request))




