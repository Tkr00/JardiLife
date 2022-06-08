from django import forms
from django.forms import ModelForm
from .models import Arbusto, Flore, Macetero, tierra_de_hojas


class ArbustoForm(ModelForm):

    class Meta:
        model = Arbusto
        fields = ['nombreArbusto','precio','categoria','upload']

class FloreForm(ModelForm):

    class Meta:
        model = Flore
        fields = ['nombreFlore','precio','categoria','upload']

class MaceteroForm(ModelForm):

    class Meta:
        model = Macetero
        fields = ['nombreMacetero','precio','categoria','upload']

class TierraForm(ModelForm):

    class Meta:
        model = Tierra_De_Hoja
        fields = ['nombreTierraDeHoja','precio','categoria','upload']