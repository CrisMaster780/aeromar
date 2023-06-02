from django.shortcuts import render
from .models import Caso, Cliente
import sweetify


def home(request):
    if request.method == "GET":
        codigo_caso = request.GET.get("caso")
        print(codigo_caso)
        caso = Caso.objects.filter(codigo_caso=codigo_caso)
        if caso:
            return render(
                request,
                "index.html",
                {
                    "codigo": caso,
                },
            )
        else:
            mensaje = "No se encontro un caso con ese Numero"
            return render(
                request,
                "index.html",
                {
                    "codigo": "",
                    "mensaje": mensaje,
                },
            )
