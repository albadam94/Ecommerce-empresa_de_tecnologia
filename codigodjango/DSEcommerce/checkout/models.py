# Create your models here.
from django.db import models

# Crear los modelos de nuestro Checkout

class carrito(models.Model):
    
    usuario = models.CharField(max_length=100)     
    dcto = models.FloatField(default=0)             
    fecha = models.DateField(auto_now_add=True, blank=True, null=True)

    #MÉTODOS
    def __str__(self):
        #permite especificar la información de los objetos en base de datos
        return self.usuario + " - " + str(self.fecha)
    
    def total(self):
        total = 0
        items = Item.objects.filter(carrito=self)
        for item in items:
            total += item.subtotal()
        return total

class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    categoria = models.CharField(choices='options', max_length=10)  
    referencia= models.CharField(max_length=100,primary_key=True,null=False)

    def __str__(self):
        #Brindar una identificación general en base de datos (sección 'Admin')
        return self.nombre

class Item (models.Model):  
    #<nomClase_minuscula>_set.all()     => ForeignKey


    #ForeignKey => establecer una conexión entre el objeto 'Item' y 'CarritoCompras'
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)        #ES un objeto del tipo producto
    carrito = models.ForeignKey('CarritoCompras', on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    
    def __str__(self):
        return self.producto.nombre
    
    def subtotal(self):
        return self.producto.precio*self.cantidad