# Create your views here.

from models import *
from django.http import HttpResponse

def alumnos_seccion(request, seccion):
	
	alumnos = Alumno.objects.filter(seccion_id=int(seccion)).order_by('apellido')	 

	return HttpResponse("<h1>Hola<h1>")




