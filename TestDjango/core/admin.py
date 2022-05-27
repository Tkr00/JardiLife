from django.contrib import admin
from .models import Categoria,Arbustos,Flores,Maceteros,Tierra_De_Hojas
# Register your models here.
#Permite administrar el modelo completo

admin.site.register(Categoria)
admin.site.register(Arbustos)
admin.site.register(Flores)
admin.site.register(Maceteros)
admin.site.register(Tierra_De_Hojas)