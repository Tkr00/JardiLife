from django.urls import path
from .views  import Pagina,inicio,Flores, Macetero, Arbustos, quienes_somos, tierra_de_hojas,p, form_produc, form_carrito, form_mod_producto, ListProduc, form_del_producto

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
    path('form_carrito/<id>',form_carrito,name='form_carrito'),
    path('form_mod_producto/<id>',form_mod_producto,name='form_mod_producto'),
    path('ListProduc/<id>',ListProduc,name='ListProduc'),
    path('form_del_producto/<id>',form_del_producto,name='form_del_producto')
]