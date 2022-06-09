from django.shortcuts import render
from .models import Categoria, Producto

# Create your views here.



def Pagina(request):
    
    return render(request,'core/Pagina.html',)
def inicio(request):
    
    return render(request,'core/inicio.html',)

def Flores(request):
    categorias = Categoria.objects.get(idCategoria=id)
    producto=Producto.objects.filter(categoria=categorias)
    return render(request,'core/Flores.html',{'categoria':categorias,'producto':producto})

def Macetero(request):
    categorias = Categoria.objects.get(idCategoria=id)
    producto=Producto.objects.filter(categoria=categorias)
    return render(request,'core/Macetero.html',{'categoria':categorias,'producto':producto})

def Arbustos(request,id):
    categorias = Categoria.objects.get(idCategoria=id)
    producto=Producto.objects.filter(categoria=categorias)
    return render(request,'core/Arbustos.html',{'categoria':categorias,'producto':producto})

def p(request):  
    return render(request,'core/p.html',)    

def quienes_somos(request):  
    return render(request,'core/quienes_somos.html',)   

def tierra_de_hojas(request):
    categorias = Categoria.objects.get(idCategoria=id)
    producto=Producto.objects.filter(categoria=categorias)
    return render(request,'core/tierra_de_hojas.html',{'categoria':categorias,'producto':producto})  


