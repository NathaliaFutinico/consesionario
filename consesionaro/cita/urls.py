from django.urls import path, include
from .views import CitaViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('cita', CitaViewSet, basename='cita')

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]
