from django.urls import path, include
from rest_framework import urlpatterns
from productos.views import * 
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('categoria',apicategoria)
router.register('marca',apimarca)
router.register('articulo',apiarticulo)

urlpatterns = [
    path('crud/',include(router.urls))
]

