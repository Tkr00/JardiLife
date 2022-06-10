from django.urls import path
from .views  import Pagina,inicio,Flores, Macetero, Arbustos, quienes_somos, tierra_de_hojas,p, form_produc, form_carrito

urlpatterns = [
    path('', Pagina, name= "Pagina" ),
    path('inicio', inicio, name="inicio"),
    path('Flores/<id>', Flores, name="Flores"),
    path('Macetero/<id>', Macetero, name="Macetero"),
    path('Arbustos/<id>', Arbustos, name="Arbustos"),
    path('quienes_somos', quienes_somos, name= "quienes_somos"),
    path('tierra_de_hojas/<id>', tierra_de_hojas,name= "tierra_de_hojas"),
    path('p', p,name="p"),
    path('form_produc/<id>',form_produc,name='form_produc'),
    path('form_carrito',form_carrito,name='form_carrito')
]