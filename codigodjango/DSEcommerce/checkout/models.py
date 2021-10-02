from django.db import models
from django.db.models.fields import BooleanField, CharField, DateTimeField
from productos.models import articulo

class carrito(models.Model):
    perfil=models.CharField(max_length=200, null=False)
    info_envio=models.CharField(max_length=200, null=False)
    fecha=models.DateField(auto_now_add=True)
    pagado=models.BooleanField(default=False)

    def __str__(self):
        return self.perfil + " - " + str(self.fecha)

    @property
    def cant_art(self):
        cant = 0
        items = producto.objects.filter(carrito=self)
        for item in items:
            cant += item.cantidad
        return cant

    @property
    def total(self):
        total = 0
        items = producto.objects.filter(carrito=self)
        for item in items:
            total+= item.subtotal
        return total

class producto (models.Model):  
    carrito = models.ForeignKey(carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(articulo, on_delete=models.SET_NULL, null=True)        
    cantidad = models.IntegerField(default=0)
    
    def __str__(self):
        return self.carrito.perfil + "(" + self.producto.nombre + ")" + "[" + str(self.cantidad)+ "]"
    
    @property
    def subtotal(self):
        return self.producto.precio*self.cantidad


