from django.db import models

# Create your models here.

#Modelo para categoria

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50,verbose_name="Nombre de la Categoria")

    def __str__(self):
        return self.nombreCategoria

#Modelo Arbustos
class Producto(models.Model):
    nombreP = models.CharField(primary_key=True,max_length=50,verbose_name='Nombre Producto')
    precio = models.CharField(max_length=6,verbose_name='Precio Arbusto')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombreP
