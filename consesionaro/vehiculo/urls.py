from django.urls import path, include
from .views import VehiculoViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('vehiculo', VehiculoViewSet, basename='vehiculo')

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]
