from .models import Cita
from .serializers import CitaSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CitaViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,) 

    
    serializer_class = CitaSerializer
    queryset = Cita.objects.all()