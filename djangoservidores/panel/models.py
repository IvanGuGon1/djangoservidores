from django.db import models

# Create your models here.
class Servidores(models.Model):

	alias = models.CharField(max_length=15, unique=True)
	distribucion = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=140)
	ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
	puerto = models.PositiveIntegerField(default=22)
	fechaCreacion = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
	usuario = models.CharField(max_length=20)
	password = models.CharField(max_length=20)

	def __str__(self):
		return self.alias