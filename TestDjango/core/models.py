from django.db import models

# Create your models here.

#Modelo para categoria

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50,verbose_name="Nombre de la Categoria")

    def __str__(self):
        return self.nombreCategoria

#Modelo Arbustos
class Arbusto(models.Model):
    nombreArbusto = models.CharField(primary_key=True,max_length=20,verbose_name='Nombre Arbusto')
    precio = models.CharField(max_length=6,verbose_name='Precio Arbusto')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    upload = models.ImageField(upload_to ='A:\Repo\SOLEMNE-1\TestDjango\core\static\core\img\img_productos',verbose_name='Subir imagen')
    
    def __str__(self):
        return self.nombreArbusto

#Modelo Flores
class Flore(models.Model):
    nombreFlore = models.CharField(primary_key=True,max_length=20,verbose_name='Nombre Flores')
    precio = models.CharField(max_length=6,verbose_name='Precio Flores')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    upload = models.ImageField(upload_to ='A:\Repo\SOLEMNE-1\TestDjango\core\static\core\img\img_productos',verbose_name='Subir imagen')

    def __str__(self):
        return self.nombreFlore

#Modelo Maceteros
class Macetero(models.Model):
    nombreMacetero = models.CharField(primary_key=True,max_length=20,verbose_name='Nombre Arbusto')
    precio = models.CharField(max_length=6,verbose_name='Precio Arbusto')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    upload = models.ImageField(upload_to ='A:\Repo\SOLEMNE-1\TestDjango\core\static\core\img\img_productos',verbose_name='Subir imagen')

    def __str__(self):
        return self.nombreMacetero

#Modelo Tierra De Hojas
class Tierra_De_Hoja(models.Model):
    nombreTierraDeHoja = models.CharField(primary_key=True,max_length=20,verbose_name='Nombre Arbusto')
    precio = models.CharField(max_length=6,verbose_name='Precio Arbusto')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    upload = models.ImageField(upload_to ='A:\Repo\SOLEMNE-1\TestDjango\core\static\core\img\img_productos',verbose_name='Subir imagen')

    def __str__(self):
        return self.nombreTierraDeHoja