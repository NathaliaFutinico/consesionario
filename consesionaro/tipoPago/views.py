from .models import Tipodepago
from .serializers import TipodepagoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class TipodePagoViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,) 

    
    serializer_class = TipodepagoSerializer
    queryset = Tipodepago.objects.all()