from django.contrib import admin

# Register your models here.

from .models import Socio, Cancha, Torneo,Reserva

admin.site.register(Socio)
admin.site.register(Cancha)
admin.site.register(Torneo)
admin.site.register(Reserva)