from django import forms
from django.forms import ModelForm
from .models import Producto


class Producform(ModelForm):

    class Meta:
        model = Producto
        fields = ['nombreP','precio','categoria','imagen','stock']