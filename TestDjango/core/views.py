from django import views
from django.shortcuts import render,redirect
from .forms import Producform
from .models import Categoria, Producto
from django.http import HttpResponse
from .carro import Carro
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
# Create your views here.



def Pagina(request):
    producto = Producto.objects.all()
    carro=Carro(request)
    return render(request,'core/Pagina.html',{'producto':producto})

def base(request):  
    return render(request,'core/base.html',)      
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

def form_carrito(request):   

    return render(request,'core/form_carrito.html')

def ListProduc(request):
    producto = Producto.objects.all()

    datos = {
        'producto': producto
    }
    return render(request,'core/ListProduc.html',datos)

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

def form_del_producto(request,id):

    producto = Producto.objects.get(nombreP=id)

    producto.delete()

    return redirect(to='ListProduc')

def agregar_producto(request, nombre):
    carro = Carro(request)
    producto=Producto.objects.get(nombreP=nombre)
    carro.agregar(producto=producto)
    return redirect(to='form_carrito')

def eliminar_producto(request, nombre):
    carro = Carro(request)
    producto=Producto.objects.get(nombreP=nombre)
    carro.eliminar(producto=producto)
    return redirect(to='form_carrito')

def restar_producto(request, nombre):
    carro = Carro(request)
    producto=Producto.objects.get(nombreP=nombre)
    carro.restar_producto(producto=producto)
    return redirect(to='form_carrito')

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect(to='form_carrito')

class Registro(View):
    def get(self, request):
        form=UserCreationForm()
        return render(request,"core/registro.html",{"form":form})
    def post(self, request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect('Pagina')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
                return render(request,"core/registro.html",{"form":form})
def cerrar_sesion(request):
    logout(request)
    return redirect('Pagina')
    
def iniciar_sesion(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre=form.cleaned_data.get("username")
            contraseña=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                return redirect('Pagina')
            else:
                messages.error(request, "Usuario no valido")
        else:
            messages.error(request,"Informacion incorrecta")
    form=AuthenticationForm()
    return render(request,"core/iniciar_sesion.html",{"form":form})