from .models import Tipovehiculo
from .serializers import TipovehiculoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class TipovehiculoViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,) 

    
    serializer_class = TipovehiculoSerializer
    queryset = Tipovehiculo.objects.all()