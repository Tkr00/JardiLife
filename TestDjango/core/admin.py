from django.contrib import admin
from .models import Categoria,Arbusto,Flore,Macetero,Tierra_De_Hoja
# Register your models here.
#Permite administrar el modelo completo

admin.site.register(Categoria)
admin.site.register(Arbusto)
admin.site.register(Flore)
admin.site.register(Macetero)
admin.site.register(Tierra_De_Hoja)