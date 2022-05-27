from django.shortcuts import render,redirect
from .forms import VehiculoForm
from .models import Vehiculo

# Create your views here.



def home(request):
    vehiculos = Vehiculo.objects.all()

    datos = {
        'vehiculos': vehiculos
    }
    return render(request,'core/home.html',datos)

def form_vehiculo(request):
    
    datos = {
        'form':VehiculoForm()
    }

    if request.method=='POST':
        formulario =  VehiculoForm(request.POST)

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente";

    return render(request,'core/form_vehiculo.html',datos)

def form_mod_vehiculo(request,id):

    vehiculo = Vehiculo.objects.get(patente=id)

    datos = {
        'form': VehiculoForm(instance=vehiculo)
    }

    if request.method == 'POST':
        formulario = VehiculoForm(data=request.POST,instance=vehiculo)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificacion realizada Correctamente"


    return render(request, 'core/form_mod_vehiculo.html',datos)

def form_del_vehiculo(request,id):

    vehiculo = Vehiculo.objects.get(patente=id)

    vehiculo.delete()

    return redirect(to='home')