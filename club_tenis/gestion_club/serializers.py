from rest_framework import serializers
from .models import Socio, Cancha, Reserva, Torneo

class SocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socio
        fields = '__all__'

class CanchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancha
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class TorneoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torneo
        fields = '__all__'
