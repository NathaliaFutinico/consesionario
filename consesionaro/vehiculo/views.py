from .models import Vehiculo
from .serializers import VehiculoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class VehiculoViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,) 

    
    serializer_class = VehiculoSerializer
    queryset = Vehiculo.objects.all()