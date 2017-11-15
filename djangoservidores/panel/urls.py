from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
	

	
	url(r'^$', views.ServidoresList.as_view(), name='servidores_list'),
	url(r'^nuevo$', views.ServidoresCreate.as_view(), name='servidores_new'),
	url(r'^editar/(?P<pk>\d+)$', views.ServidoresUpdate.as_view(), name='servidores_edit'),
	url(r'^eliminar/(?P<pk>\d+)$', views.ServidoresDelete.as_view(), name='servidores_delete'),



]