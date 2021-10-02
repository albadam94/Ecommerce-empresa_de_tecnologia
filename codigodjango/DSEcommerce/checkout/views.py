from django.db.models.query import QuerySet
from rest_framework import viewsets, views, authentication, permissions
from rest_framework.response import Response
from checkout.serializers import *
from checkout.models import *

class carritoapi (viewsets.ModelViewSet):
    serializer_class = carrito_serial
    queryset = carrito.objects.all()

class productoapi (viewsets.ModelViewSet):
    serializer_class = producto_serial
    queryset = producto.objects.all()
