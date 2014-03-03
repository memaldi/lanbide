from django.shortcuts import render
from paro.models import Municipio

# Create your views here.

def infoMunicipio(request, id_municipio):
    municipio = Municipio.objects.get(id=id_municipio)
    datos = municipio.datosparo_set.all()
    context = {}
    lista_datos = []
    for dato in datos:
        porcentaje_paro = round(float(dato.parados) / dato.poblacion_activa * 100, 2)
        lista_datos.append((dato.ano, dato.trimestre, porcentaje_paro)) 
    context['lista_datos'] = lista_datos
    return render(request, 'paro/municipio.html', context)
    
def mapa(request):
    municipios = Municipio.objects.all()
    context = {}
    for municipio in municipios:
        datos_paro = municipio.datosparo_set.filter(ano=2013, trimestre=4)
        
