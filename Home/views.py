from django.shortcuts import render
from .models import Caso, Cliente
import sweetify


def home(request):
    if request.method == "POST":
        codigo_caso = request.POST.get("caso")
        print(codigo_caso)
        caso = Caso.objects.filter(codigo_caso=codigo_caso)
        if caso:
            return render(
                request,
                "index.html",
                {
                    "codigo": caso,
                    "consulta_cliente":'ConsultaCliente'
                },
            )
        else:
            mensaje = "No se encontró un caso con ese Número de Caso"
            return render(
                request,
                "index.html",
                {
                    "codigo": "",
                    
                    "mensaje": mensaje,
                },
            )
    else:
        return render(
            request,
            "index.html",
        )
    
def correo(request):
    if request.method == "POST":
        correo_caso = request.POST.get("correo")
        print(correo_caso)
        caso = Caso.objects.filter(cliente__correo=correo_caso)
        if caso:
            return render(
                request,
                "consulta_correo.html",
                {
                    "codigo": caso,
                    "consulta_correo":'ConsultaCorreo'
                },
            )
        else:
            mensaje = "No se encontró ningún caso asociado a ese Correo"
            return render(
                request,
                "consulta_correo.html",
                {
                    "codigo": "",
                    "mensaje": mensaje,
                },
            )
    else:
        return render(
            request,
            "consulta_correo.html",
        )

