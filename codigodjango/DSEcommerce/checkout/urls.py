from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import urlpatterns
from checkout.views import *

router = DefaultRouter()
router.register('carrito',carritoapi)
router.register('producto',productoapi)

urlpatterns=[
    path('crud/',include(router.urls))
]