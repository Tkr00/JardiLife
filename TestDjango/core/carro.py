
class Carro:
    def __init__(self, request):
        ''''self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
        else:'''
        self.carro=carro
    def agregar(self, producto):
        if(producto.nombreP not in self.carro.keys()):
            self.carro[producto.nombreP]={
                "nombre":producto.nombreP,
                "precio":str(producto.precio),
                "imagen":producto.imagen.url,
                "cantidad":1
            }
        else:
            for key, value in self.carro.items():
                if key==producto.nombreP:
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"])+float(producto.precio)
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True
    def eliminar(self, producto):
        producto.nombreP=producto.nombreP
        if producto.nombreP in self.carro:
            del self.carro[producto.nombreP]
            self.guardar_carro()
    def restar_producto(self, producto):
        for key, value in self.carro.items():
                if key==producto.nombreP:
                    value["cantidad"]=value["cantidad"]-1
                    value["precio"]=float(value["precio"])-float(producto.precio)
                    if value["cantidad"]<1:
                        self.eliminar(producto)
                    break
        self.guardar_carro()  
    def limpiar_carro(self):
        carro=self.session["carro"]={}
        self.session.modified=True
        