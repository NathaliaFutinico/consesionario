from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,) 

    
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()