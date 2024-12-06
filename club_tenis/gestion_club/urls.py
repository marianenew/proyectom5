from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SocioViewSet, CanchaViewSet, ReservaViewSet, TorneoViewSet, 
    CanchasDisponibles, TotalReservasPorSocio
)

router = DefaultRouter()
router.register(r'socios', SocioViewSet)
router.register(r'canchas', CanchaViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'torneos', TorneoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('canchas-disponibles/', CanchasDisponibles.as_view()),
    path('reservas/total/<int:socio_id>/', TotalReservasPorSocio.as_view(), name='total_reservas_socio'),
]
