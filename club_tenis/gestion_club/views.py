from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Socio, Cancha, Reserva, Torneo
from .serializers import SocioSerializer, CanchaSerializer, ReservaSerializer, TorneoSerializer

class SocioViewSet(viewsets.ModelViewSet):
    queryset = Socio.objects.all()
    serializer_class = SocioSerializer

class CanchaViewSet(viewsets.ModelViewSet):
    queryset = Cancha.objects.all()
    serializer_class = CanchaSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class TorneoViewSet(viewsets.ModelViewSet):
    queryset = Torneo.objects.all()
    serializer_class = TorneoSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cancha

class CanchasDisponibles(APIView):
    def get(self, request):
        disponibles = Cancha.objects.filter(disponible=True)
        serializer = CanchaSerializer(disponibles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Esta API recibe el socio_id como parámetro en la URL, busca al socio, y cuenta cuántas reservas tiene asociadas.

class TotalReservasPorSocio(APIView):
    def get(self, request, socio_id):
        try:
            socio = Socio.objects.get(id=socio_id)
            total_reservas = Reserva.objects.filter(socio=socio).count()
            return Response(
                {"socio": socio.nombre, "total_reservas": total_reservas},
                status=status.HTTP_200_OK
            )
        except Socio.DoesNotExist:
            return Response(
                {"error": "Socio no encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )
