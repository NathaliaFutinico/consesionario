from .models import Empleado
from .serializers import EmpleadoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class EmpleadoViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,) 

    
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()