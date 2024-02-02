from django.shortcuts import render
from restoManager_app.models import Servicio
from restoManager_app.models import ServiEjemplo
# Create your views here.

""" 
mesa += {
    "mesa"+i: [mesaID, [Plato],  ],
}
 """

def mesas(request):
    totalDeMEsas = ServiEjemplo.objects.filter(max)
    diccionario = {}
    # while (totalDeMesas)
    for i in range(totalDeMEsas):
        query = ServiEjemplo.objects.filter(mesaID=i+1)
        for i in query:
            print(i)
        print(query)
        diccionario["mesa"+str(i+1)] = query

    return render(request, "secciones/mesas.html", diccionario)


""" def activarPlatos(request):
    return render(request)

def activarPlatos(request):
    return render(request)

def activarPlatos(request):
    return render(request)
"""

def avisos(request):
    return render(request, "secciones/avisos.html")