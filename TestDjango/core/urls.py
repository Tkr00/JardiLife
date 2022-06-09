from django.urls import path
from .views  import Pagina,inicio,Flores, Macetero, Arbustos, quienes_somos, tierra_de_hojas,p

urlpatterns = [
    path('', Pagina, name= "Pagina" ),
    path('inicio', inicio, name="inicio"),
    path('Flores', Flores, name="Flores"),
    path('Macetero', Macetero, name="Macetero"),
    path('Arbustos/<id>', Arbustos, name="Arbustos"),
    path('quienes_somos', quienes_somos, name= "quienes_somos"),
    path('tierra_de_hojas', tierra_de_hojas,name= "tierra_de_hojas"),
    path('p', p,name="p")
]