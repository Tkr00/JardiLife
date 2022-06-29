from django.urls import path
from rest_jardi.views import lista_producto,detalle_producto

urlpatterns = [
    path('lista_producto', lista_producto, name="lista_producto"),
    path('detalle_producto/<id>', detalle_producto, name="detalle_producto")
]