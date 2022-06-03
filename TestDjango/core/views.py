from django.shortcuts import render

# Create your views here.



def Pagina(request):
    
    return render(request,'core/Pagina.html',)
def inicio(request):
    
    return render(request,'core/inicio.html',)
def Flores(request):
    flores = Flores.objects.all()

    datos = {
        'flores': flores
    }
    return render(request,'core/Flores.html',)
def Macetero(request):
    Macetero = Macetero.objects.all()

    datos = {
        'macetero': macetero
    }
    return render(request,'core/Macetero.html',)
def Arbustos(request):
    arbustos = Arbustos.objects.all()

    datos = {
        'arbustos': arbustos
    }
    return render(request,'core/Arbustos.html',)
def Producto(request):
    
    return render(request,'core/Producto.html',)    
def quienes_somos(request):
    
    return render(request,'core/quienes_somos.html',)   
def tierra_de_hojas(request):
    tierra_de_hojas = Tierra_de_hojas.objects.all()

    datos = {
        'tierra_de_hojas': tierra_de_hojas
    }
    return render(request,'core/tierra_de_hojas.html',)     

