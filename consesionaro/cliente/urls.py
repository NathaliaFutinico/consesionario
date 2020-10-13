from django.urls import path, include
from .views import ClienteViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('cliente', ClienteViewSet, basename='cliente')

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]
