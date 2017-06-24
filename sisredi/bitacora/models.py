from __future__ import unicode_literals

from django.db import models

# Create your models here.
class reporte(models.Model):
	fecha = models.DateTimeField(auto_now_add=True, auto_now=False)
	agente = models.CharField(max_length=15, blank=True, null=True)
	ambiente = models.CharField(max_length=15, blank=True, null=True)
	#email = models.EmailField(blank=True)
	suitedpto = models.CharField(max_length=15, blank=True, null=True)
	reporta = models.CharField(max_length=15, blank=True, null=True)
	areaatencion = models.CharField(max_length=15, blank=True, null=True)
	descripcion = models.TextField(verbose_name='descripcion')
	solucion = models.CharField(max_length=100, blank=True, null=True)
	status = models.CharField(max_length=10, blank=True, null=True)
	#media = models.FileField(upload_to='myfolder/', blank=True, null=True)
	#ambiente timestamp
	#area
	
	#python 2
	#def_unicode_(self):
	  #  return self.email

	#python 3
	#def publish(self):
	#	self.publish_date = timezone.now()
	#	self.save


	def _str_(self):
		return self.agente
