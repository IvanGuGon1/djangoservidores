from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from panel.models import Servidores


def ServidoresList(request):
	servidores = Servidores.objects.all()
	"""
	Lanzar un ping. Si true, enviar la informacion al template para mostar On y Off
	Opcion 1
	import subprocess, platform
	def pingOk(sHost):
    	try:
        	output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower()=="windows" else 'c', sHost), shell=True)

    	except Exception:
        	return False

    	return True
	
    	import os, sys
		host = "8.8.8.8"
		os.system("ping " + ("-n 1 " if  sys.platform().lower()=="win32" else "-c 1 ") + host)
	"""
	data = {}
	data['object_list'] = servidores
	return render(request, "servidores_list.html", data)

class ServidoresList(ListView):

    model = Servidores

class ServidoresCreate(CreateView):
    model = Servidores
    success_url = reverse_lazy('servidores_list')
    fields = ['alias', 'distribucion', 'descripcion', 'ip', 'puerto', 'usuario', 'password']

class ServidoresUpdate(UpdateView):
    model = Servidores
    success_url = reverse_lazy('servidores_list')
    fields = ['alias', 'distribucion', 'descripcion', 'ip', 'puerto', 'usuario', 'password']

class ServidoresDelete(DeleteView):
    model = Servidores
    success_url = reverse_lazy('servidores_list')