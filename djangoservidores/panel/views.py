from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from panel.models import Servidores



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