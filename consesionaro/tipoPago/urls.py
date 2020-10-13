from django.urls import path, include
from .views import TipodePagoViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('tipoPago', TipodePagoViewSet, basename='tipoPago')

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]
