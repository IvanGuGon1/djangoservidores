

# Register your models here.
from django.contrib import admin
from .models import Servidores



class ServidoresAdmin(admin.ModelAdmin):
    pass
admin.site.register(Servidores, ServidoresAdmin)