from django.shortcuts import render


def home(request):
    if request.method == 'GET':
        codigo_caso = request.GET.get('caso')
        print(codigo_caso)
        caso = [
            'CAS-PRUEBA',
            'PRUEBA CRISTOBAL'
            'ACTIVO',
            'REPUESTOS'
        ]
        if caso[0] == codigo_caso:

            return render(request, 'index.html', {
                "codigo": caso,
            })
        else:
            print("El código del caso no existe en el diccionario.")
            return render(request, 'index.html', {
                "codigo": '',
            })
