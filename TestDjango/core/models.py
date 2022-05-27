from django.db import models

# Create your models here.

#Modelo para categoria

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50,verbose_name="Nombre de la Categoria")

    def __str__(self):
        return self.nombreCategoria

#Modelo Arbustos
class Arbustos(models.Model):
    nombreArbustos = models.CharField(primary_key=True,max_length=20,verbose_name='Nombre Arbusto')
    precio = models.CharField(max_length=6,verbose_name='Precio Arbusto')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombreArbustos

#Modelo Flores
class Flores(models.Model):
    nombreFlores = models.CharField(primary_key=True,max_length=20,verbose_name='Nombre Flores')
    precio = models.CharField(max_length=6,verbose_name='Precio Flores')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreFlores

#Modelo Maceteros
class Maceteros(models.Model):
    nombreMaceteros = models.CharField(primary_key=True,max_length=20,verbose_name='Nombre Arbusto')
    precio = models.CharField(max_length=6,verbose_name='Precio Arbusto')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreMaceteros

#Modelo Tierra De Hojas
class Tierra_De_Hojas(models.Model):
    nombreTierraDeHojas = models.CharField(primary_key=True,max_length=20,verbose_name='Nombre Arbusto')
    precio = models.CharField(max_length=6,verbose_name='Precio Arbusto')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreTierraDeHojas