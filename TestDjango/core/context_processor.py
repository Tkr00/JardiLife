def total_carro(request):
    total=1000
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total=total+(float(value["precio"])*value["cantidad"])
    return {"total_carro":total}