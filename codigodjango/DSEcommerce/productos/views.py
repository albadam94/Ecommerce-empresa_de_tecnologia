from rest_framework import viewsets
from productos.models import *
from productos.serializers import *

class apicategoria (viewsets.ModelViewSet):
    serializer_class = categoria_serial
    queryset = categoria.objects.all()

class apimarca(viewsets.ModelViewSet):
    serializer_class = marca_serial
    queryset = marca.objects.all()

class apiarticulo (viewsets.ModelViewSet):
    serializer_class = articulo_serial
    queryset = articulo.objects.all()
