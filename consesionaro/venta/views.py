from .models import Venta
from .serializers import VentaSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class VentaViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,) 

    
    serializer_class = VentaSerializer
    queryset = Venta.objects.all()