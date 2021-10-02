from django.db.models import fields
from django.db.models.base import Model
from checkout.models import *
from rest_framework import serializers

class carrito_serial(serializers.ModelSerializer):
    class Meta:
        model=carrito
        fields=["perfil","info_envio","fecha","pagado","cant_art","total"]

class producto_serial(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=producto
        fields=["carrito","producto","cantidad","subtotal"]