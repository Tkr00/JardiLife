from django.shortcuts import render

# Create your views here.
class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()


def home(request):
    
    lista = ["Burger","McDonald","PDG","JM"]
    hijo = Persona("Fernando Rivera","4")
    contexto={"nombre":"Jose Riquelme","comidas":lista,"hijo":hijo}
    return render(request,'core/home.html',contexto)