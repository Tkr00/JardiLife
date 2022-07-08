from cgitb import html
from tokenize import Name
from unicodedata import name
from django import views
from django.urls import path
from .views  import ListTierra_de_hojas, ListFlores, Pagina, cerrar_sesion, form_agregar, form_del_Arbusto, form_del_Flores, form_del_Macetero, form_del_Tierra_de_hojas, iniciar_sesion,Flores, Macetero, Arbustos, quienes_somos, Registro, tierra_de_hojas,p, form_produc, form_carrito, form_mod_producto, ListArbusto, agregar_producto, eliminar_producto, restar_producto, limpiar_carro, base, ListMacetero

urlpatterns = [
    path('', Pagina, name= "Pagina" ),
    path('iniciar_sesion', iniciar_sesion, name="iniciar_sesion"),
    path('Flores/<id>', Flores, name="Flores"),
    path('Macetero/<id>', Macetero, name="Macetero"),
    path('Arbustos/<id>', Arbustos, name="Arbustos"),
    path('quienes_somos', quienes_somos, name= "quienes_somos"),
    path('tierra_de_hojas/<id>', tierra_de_hojas,name= "tierra_de_hojas"),
    path('p', p,name="p"),
    path('form_produc/<id>',form_produc,name='form_produc'),
    path('form_carrito',form_carrito,name='form_carrito'),
    path('form_mod_producto/<id>',form_mod_producto,name='form_mod_producto'),
    path('ListArbusto/<id>',ListArbusto,name='ListArbusto'),
    path('ListMacetero/<id>',ListMacetero,name='ListMacetero'),
    path('ListFlores/<id>',ListFlores,name='ListFlores'),
    path('ListTierra_de_hojas/<id>',ListTierra_de_hojas,name='ListTierra_de_hojas'),
    path('form_del_Arbusto/<id>',form_del_Arbusto,name='form_del_Arbusto'),
    path('form_del_Macetero/<id>',form_del_Macetero,name='form_del_Macetero'),
    path('form_del_Flores/<id>',form_del_Flores,name='form_del_Flores'),
    path('form_del_Tierra_de_hojas/<id>',form_del_Tierra_de_hojas,name='form_del_Tierra_de_hojas'),
    path('agregar/<nombre>',agregar_producto, name="agregar"),
    path('eliminar/<nombre>',eliminar_producto , name="eliminar"),
    path('restar/<nombre>',restar_producto , name="restar"),
    path('limpiar',limpiar_carro, name="limpiar"),
    path('registro',Registro.as_view(),name='registro'),
    path('cerrar_sesion',cerrar_sesion,name="cerrar_sesion"),
    path('base', base, name="base"),
    path('form_agregar',form_agregar,name="form_agregar")
]