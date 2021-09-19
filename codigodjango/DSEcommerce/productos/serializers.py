from productos.models import * 
from rest_framework import serializers

class categoria_serial(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = ('nombre','num_articulos')

class marca_serial(serializers.ModelSerializer):
    class Meta:
        model = marca
        fields = ('nombre','num_articulos')

class articulo_serial(serializers.ModelSerializer):
    class Meta:
        model = articulo
        fields = ('referencia','marca','categoria','precio')