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
	asistencias = models.ManyToManyField("Clase", through="Asistencia")

	def __unicode__(self):		
		return self.nombre


class Asistencia(models.Model):

	alumno = models.ForeignKey("Alumno")
	clase = models.ForeignKey("Clase")
	punto = models.BooleanField()   




class Clase(Model):

	LUGARES = (
		('L', 'Laboratorio'),
		('S', 'Salón de clases')
	)

	descripcion = models.TextField(blank=True, help_text='Lo que se dio en la clase')
	fecha = models.DateField(help_text='La fecha de la clase')
	lugar = models.CharField(max_length=1, choices=LUGARES, default='L')


	def __unicode__(self):
		return "Clase del " + str(self.fecha)

