from django.urls import path, include
from .views import TipovehiculoViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('tipoVehiculo', TipovehiculoViewSet, basename='tipoVehiculo')

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]
