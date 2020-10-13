from django.urls import path, include
from .views import EmpleadoViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('empleado', EmpleadoViewSet, basename='empleado')

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]
