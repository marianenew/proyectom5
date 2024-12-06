from django.db import models

# Create your models here.

from django.core.exceptions import ValidationError
from datetime import date

# Modelo de Socio
class Socio(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()

    # Validación personalizada: Los socios deben tener al menos 16 años
    def clean(self):
        edad = (date.today() - self.fecha_nacimiento).days // 365
        if edad < 16:
            raise ValidationError("El socio debe tener al menos 16 años.")

    def __str__(self):
        return self.nombre


# Modelo de Cancha
class Cancha(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50, choices=[('arcilla', 'Arcilla'), ('césped', 'Césped'), ('dura', 'Dura')])
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - {self.tipo}"


# Modelo de Reserva
class Reserva(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    # Validación personalizada: La reserva no puede durar más de 2 horas
    def clean(self):
        duracion = (self.hora_fin.hour - self.hora_inicio.hour) * 60 + (self.hora_fin.minute - self.hora_inicio.minute)
        if duracion > 120:
            raise ValidationError("La reserva no puede durar más de 2 horas.")

    def __str__(self):
        return f"Reserva de {self.socio.nombre} en {self.cancha.nombre}"


# Modelo de Torneo
class Torneo(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    premio = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
