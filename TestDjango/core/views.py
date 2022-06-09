from django.shortcuts import render
from .models import Producto

# Create your views here.



def Pagina(request):
    
    return render(request,'core/Pagina.html',)
def inicio(request):
    
    return render(request,'core/inicio.html',)

def Flores(request):
    return render(request,'core/Flores.html',)

def Macetero(request):
    return render(request,'core/Macetero.html',)

def Arbustos(request):
    producto = Producto.objects.all()
    
    datos = {
        'producto':producto
    }


    return render(request,'core/Arbustos.html',datos)

def p(request):  
    return render(request,'core/p.html',)    

def quienes_somos(request):  
    return render(request,'core/quienes_somos.html',)   

def tierra_de_hojas(request):
    return render(request,'core/tierra_de_hojas.html',)  


