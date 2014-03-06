from django.shortcuts import render
from paro.models import Municipio, Provincia

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
    context['nombre'] = municipio.nombre
    return render(request, 'paro/municipio.html', context)

def mapa(request):
    municipios = Municipio.objects.all()
    context = {}
    lista_municipios = []
    for municipio in municipios:
        datos_paro = municipio.datosparo_set.get(ano=2013, trimestre=4)
        porcentaje_paro = round(float(datos_paro.parados) / datos_paro.poblacion_activa * 100, 2)
        lista_municipios.append([municipio.id, municipio.nombre, porcentaje_paro, datos_paro.poblacion_activa])
    context['lista_municipios'] = lista_municipios
    return render(request, 'paro/mapa.html', context)

def provincias(request):
    provincias = Provincia.objects.all()
    context = {}
    for provincia in provincias:
        comarcas = provincia.comarca_set.all()
        poblacion_activa = 0
        parados = 0
        for comarca in comarcas:
            municipios = comarca.municipio_set.all()
            for municipio in municipios:
                datos_paro = municipio.datosparo_set.get(ano=2013, trimestre=4)
                poblacion_activa += datos_paro.poblacion_activa
                parados += datos_paro.parados
        porcentaje_paro = round(float(parados) / poblacion_activa * 100, 2)
        print provincia.nombre
        print poblacion_activa, parados
        context[provincia.nombre] = porcentaje_paro
    print context
    return render(request, 'paro/provincias.html', context)
