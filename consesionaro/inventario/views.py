from .models import Inventario
from .serializers import InventarioSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class InventarioViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,) 

    
    serializer_class = InventarioSerializer
    queryset = Inventario.objects.all()