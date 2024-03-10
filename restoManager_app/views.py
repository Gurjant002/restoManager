from django.shortcuts import render
# Create your views here.

def mesas(request):
    # query = ServiEjemplo.objects.all()
    diccionario = {}
    # diccionario["mesas"] = query

    # mesas = []
    # for i in query:
    #     num = i.mesaID
    #     mesas.append(num)
    
    # mesas = list(dict.fromkeys(mesas))
    # for i in mesas:
    #     diccionario["query"+str(i)] = ServiEjemplo.objects.filter(mesaID = i)
    # print(diccionario)
    variables = {}
    variables["diccionario"] = diccionario
    return render(request, "secciones/mesas.html", variables)


""" def activarPlatos(request):
    return render(request)

def activarPlatos(request):
    return render(request)

def activarPlatos(request):
    return render(request)
"""

def avisos(request):
    return render(request, "secciones/avisos.html")