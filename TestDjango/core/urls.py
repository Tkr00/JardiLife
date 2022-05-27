from django.urls import path
from .views  import Pagina, inicio, Flores, Macetero, Arbustos, Producto, quienes_somos, tierra_de_hojas

urlpatterns = [
    path('pagina', Pagina, name= "Pagina" ),
    path('inicio', inicio, name="inicio"),
    path('flores', Flores, name="Flores"),
    path('macetero', Macetero, name="Macetero"),
    path('arbustos', Arbustos, name="Arbustos"),
    path('producto', Producto, name="Producto"),
    path('quienes-somos', quienes_somos, name= "quienes_somos"),
    path('tierra-de-hojas', tierra_de_hojas,name= "tierra_de_hojas")
]