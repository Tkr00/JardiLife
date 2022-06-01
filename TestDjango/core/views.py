from django.shortcuts import render

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
    
    return render(request,'core/Arbustos.html',)
def Producto(request):
    
    return render(request,'core/Producto.html',)    
def quienes_somos(request):
    
    return render(request,'core/quienes_somos.html',)   
def tierra_de_hojas(request):
    
    return render(request,'core/tierra_de_hojas.html',)     

