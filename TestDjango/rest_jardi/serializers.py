from dataclasses import fields
from importlib.metadata import files
from rest_framework import serializers
from core.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombreP','precio','categoria','imagen','stock']

