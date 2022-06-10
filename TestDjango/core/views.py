from django.shortcuts import render
from .forms import Producform
from .models import Categoria, Producto
from django.http import HttpResponse

# Create your views here.



def Pagina(request):
    producto = Producto.objects.all()
    return render(request,'core/Pagina.html',{'producto':producto})
def inicio(request):
    
    return render(request,'core/inicio.html',)

def Flores(request,id):
    categorias = Categoria.objects.get(idCategoria=id)
    producto=Producto.objects.filter(categoria=categorias)
    return render(request,'core/Flores.html',{'categoria':categorias,'producto':producto})

def Macetero(request,id):
    categorias = Categoria.objects.get(idCategoria=id)
    producto=Producto.objects.filter(categoria=categorias)
    return render(request,'core/Macetero.html',{'categoria':categorias,'producto':producto})

def Arbustos(request,id):
    categorias = Categoria.objects.get(idCategoria=id)
    producto=Producto.objects.filter(categoria=categorias)
    return render(request,'core/Arbustos.html',{'categoria':categorias,'producto':producto})

def p(request):  
    producto = Producto.objects.all()
    return render(request,'core/p.html',{'producto': producto})    

def quienes_somos(request):  
    return render(request,'core/quienes_somos.html',)   

def tierra_de_hojas(request,id):
    categorias = Categoria.objects.get(idCategoria=id)
    producto=Producto.objects.filter(categoria=categorias)
    return render(request,'core/tierra_de_hojas.html',{'categoria':categorias,'producto':producto})  

def form_produc(request,id):
    nombre = Producto.objects.get(nombreP=id)
    producto=Producto.objects.filter(nombreP=nombre)

    return render(request,'core/form_produc.html',{'producto':producto})

def form_carrito(request,id):   
    nombre = Producto.objects.get(nombreP=id)
    producto=Producto.objects.filter(nombreP=nombre)
    return render(request,'core/form_carrito.html',{'producto':producto})

def form_mod_producto(request,id):

    producto = Producto.objects.get(nombreP=id)

    datos = {
        'form': Producform(instance=producto)
    }

    if request.method == 'POST':
        formulario = Producform(data=request.POST,instance=producto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificacion realizada Correctamente"

    return render(request, 'core/form_mod_producto.html',datos)
