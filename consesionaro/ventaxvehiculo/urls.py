from django.urls import path, include
from .views import VentaxvehiculoViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('ventaxvehiculo', VentaxvehiculoViewSet, basename='ventaxvehiculo')

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]
