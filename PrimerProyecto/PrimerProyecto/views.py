from django.http import HttpResponse
import datetime


def saludo(request):
    return HttpResponse("Hola Mundo")


def despedida(request):
    return HttpResponse("Adiós Mundo")


def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    return HttpResponse(fecha_actual)


def calculaEdad(request,edad, anho):

    periodo = anho - 2021
    edadFutura = edad + periodo
    documento = "En el año %s tendras %s años" % (anho, edadFutura)
    return HttpResponse(documento)
