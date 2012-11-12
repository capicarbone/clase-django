#encoding:utf-8

from django.db import models
from django.db.models import Model

class Seccion(Model):

	PROFESORES = (
		( 'AL', 'Andrés Lillo' ),
		( 'OS' , 'Oscar Salazar' )
	)

	MATERIAS = (
		('PII' , 'Programación II'),
		('EDT' , 'Estructura de datos'),
		('PRI' , 'Programación I')
	)

	numero = models.IntegerField()
	materia = models.CharField(max_length=3, choices=MATERIAS)
	profesor = models.CharField(max_length=2, choices=PROFESORES)

	class Meta:
		verbose_name_plural = 'Secciones'


class Alumno(Model):

	nombre = models.CharField(max_length=30, help_text='Nombre del alumno')
	apellido = models.CharField(max_length=30, help_text='Apellido del alumno')
	cedula = models.CharField(max_length=9, help_text='Comienze con tipo de cédula')
	seccion = models.ForeignKey("Seccion")

	def __unicode__():
		return " %s %s " % (nombre, apellido)