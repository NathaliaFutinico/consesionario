from .models import Ventaxvehiculo
from .serializers import VentaxvehiculoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class VentaxvehiculoViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,) 

    
    serializer_class = VentaxvehiculoSerializer
    queryset = Ventaxvehiculo.objects.all()