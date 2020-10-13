from django.urls import path, include
from .views import VentaViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('venta', VentaViewSet, basename='venta')

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]
