from django.shortcuts import render
from paro.models import Municipio, Provincia, DatosParo
from django.http import HttpResponse
from django.utils.datastructures import SortedDict
from django.core.cache import cache
import json
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

def _calcularParoAnual(ano=2013, trimestre=4):
    provincias = Provincia.objects.all()
    context = {}
    for provincia in provincias:
        comarcas = provincia.comarca_set.all()
        poblacion_activa = 0
        parados = 0
        for comarca in comarcas:
            municipios = comarca.municipio_set.all()
            for municipio in municipios:
                try:
                    datos_paro = municipio.datosparo_set.get(ano=ano, trimestre=trimestre)
                    poblacion_activa += datos_paro.poblacion_activa
                    parados += datos_paro.parados
                except:
                    pass
        porcentaje_paro = round(float(parados) / poblacion_activa * 100, 2)
        print provincia.nombre
        print poblacion_activa, parados
        context[provincia.nombre] = porcentaje_paro
    return context

def _cargarGrafico():
    provincias = Provincia.objects.all()
    context = {}
    datos_paro = DatosParo.objects.all().order_by('ano', 'trimestre')
    fecha_list = []
    for dp in datos_paro:
        #print dp.ano, dp.trimestre
        if (dp.ano, dp.trimestre) not in fecha_list:
            fecha_list.append((dp.ano, dp.trimestre))
    dict_paro = SortedDict()
    for fecha in fecha_list:
        dict_paro[fecha] = {}
        for provincia in Provincia.objects.all():
            poblacion_activa = 0
            parados = 0
            #dict_poblacion_parados[fecha][provincia.nombre] =
            for comarca in provincia.comarca_set.all():
                for municipio in comarca.municipio_set.all():
                    try:
                        datos_paro = municipio.datosparo_set.get(ano=fecha[0], trimestre=fecha[1])
                        poblacion_activa += datos_paro.poblacion_activa
                        parados += datos_paro.parados
                    except:
                        pass
            porcentaje_paro = round(float(parados) / poblacion_activa * 100, 2)
            dict_paro[fecha][provincia.nombre] = porcentaje_paro

    return dict_paro

def provincias(request):
    if request.POST:
        json_args = json.loads(request.POST['json'])
        print json_args
        context = _calcularParoAnual(ano=int(json_args['ano']), trimestre=int(json_args['trimestre']))
        response = '{"bizkaia": %s, "gipuzkoa": %s, "araba": %s}' % (context['BIZKAIA'], context['GIPUZKOA'], context['ARABA'])
        print response
        return HttpResponse(response)
    else:
        context = _calcularParoAnual()
        context['data'] = cache.get('grafico-provincias')
        if context['data'] == None:
            context['data'] = _cargarGrafico()
            cache.set('grafico-provincias', context['data'], None)
        print context
        return render(request, 'paro/provincias.html', context)
