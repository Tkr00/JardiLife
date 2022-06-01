from django.urls import path
from .views  import Pagina,inicio,Flores, Macetero, Arbustos, Producto, quienes_somos, tierra_de_hojas

urlpatterns = [
    path('', Pagina, name= "Pagina" ),
    path('inicio', inicio, name="inicio"),
    path('Flores', Flores, name="Flores"),
    path('Macetero', Macetero, name="Macetero"),
    path('Arbustos', Arbustos, name="Arbustos"),
    path('Producto', Producto, name="Producto"),
    path('quienes-somos', quienes_somos, name= "quienes_somos"),
    path('tierra-de-hojas', tierra_de_hojas,name= "tierra_de_hojas")
]