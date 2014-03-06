from paro.models import Municipio, Comarca, Provincia, DatosParo, DatosEdad, DatosEstudios
import sys

INPUT_FILE = '/home/mikel/open_data/lanbide/datos/Dap_Historicos09.csv'

f = open(INPUT_FILE, 'r')

i = 1
count = 1

for line in f:
    if i <= 2:
        i += 1
    else:
        sline = line.split(';')
        datos_paro = DatosParo()
        datos_paro.ano = int(sline[0])
        datos_paro.trimestre = int(sline[1])
        try:
            provincia = Provincia.objects.get(codigo=int(sline[2].replace('\'', '')))
        except:
            provincia = Provincia()
            provincia.codigo = int(sline[2].replace('\'', ''))
            provincia.nombre = sline[3]
            provincia.save()
        try:
            comarca = Comarca.objects.get(codigo=int(sline[4].replace('\'', '')))
        except:
            comarca = Comarca()
            comarca.codigo = int(sline[4].replace('\'', ''))
            comarca.nombre = sline[5]
            comarca.provincia = provincia
            comarca.save()
        try:
            municipio = Municipio.objects.get(codigo=int(sline[8].replace('\'', '')))
        except:
            municipio = Municipio()
            municipio.codigo = int(sline[8].replace('\'', ''))
            municipio.nombre = sline[9]
            municipio.comarca = comarca
            municipio.save()
        datos_paro.municipio = municipio
        datos_paro.poblacion_total = sline[10]
        datos_paro.poblacion_activa = int(float(sline[11].replace(',', '.')))
        datos_paro.parados = int(sline[12])
        datos_paro.save()
        # Hombres
        datos_edad = DatosEdad()
        datos_edad.edad = DatosEdad._20
        datos_edad.valor = sline[13]
        datos_edad.sexo = DatosEdad.HOMBRE
        datos_edad.datos_paro = datos_paro
        datos_edad.save()
        datos_edad = DatosEdad()
        datos_edad.edad = DatosEdad._20_24
        datos_edad.valor = sline[14]
        datos_edad.sexo = DatosEdad.HOMBRE
        datos_edad.datos_paro = datos_paro
        datos_edad.save()
        datos_edad = DatosEdad()
        datos_edad.edad = DatosEdad._25_29
        datos_edad.valor = sline[15]
        datos_edad.sexo = DatosEdad.HOMBRE
        datos_edad.datos_paro = datos_paro
        datos_edad.save()
        datos_edad = DatosEdad()
        datos_edad.edad = DatosEdad._30_34
        datos_edad.valor = sline[16]
        datos_edad.sexo = DatosEdad.HOMBRE
        datos_edad.datos_paro = datos_paro
        datos_edad.save()
        datos_edad = DatosEdad()
        datos_edad.edad = DatosEdad._35_39
        datos_edad.valor = sline[17]
        datos_edad.sexo = DatosEdad.HOMBRE
        datos_edad.datos_paro = datos_paro
        datos_edad.save()
        datos_edad = DatosEdad()
        datos_edad.edad = DatosEdad._40_44
        datos_edad.valor = sline[18]
        datos_edad.sexo = DatosEdad.HOMBRE
        datos_edad.datos_paro = datos_paro
        datos_edad.save()
        datos_edad = DatosEdad()
        datos_edad.edad = DatosEdad._45_49
        datos_edad.valor = sline[19]
        datos_edad.sexo = DatosEdad.HOMBRE
        datos_edad.datos_paro = datos_paro
        datos_edad.save()
        datos_edad = DatosEdad()
        datos_edad.edad = DatosEdad._50_54
        datos_edad.valor = sline[20]
        datos_edad.sexo = DatosEdad.HOMBRE
        datos_edad.datos_paro = datos_paro
        datos_edad.save()
        datos_edad = DatosEdad()
        datos_edad.edad = DatosEdad._55_59
        datos_edad.valor = sline[21]
        datos_edad.sexo = DatosEdad.HOMBRE
        datos_edad.datos_paro = datos_paro
        datos_edad.save()
        datos_edad = DatosEdad()
        datos_edad.edad = DatosEdad._59
        datos_edad.valor = sline[22]
        datos_edad.sexo = DatosEdad.HOMBRE
        datos_edad.datos_paro = datos_paro
        datos_edad.save()
        # Mujeres
        datos_edad = DatosEdad()
        datos_edad.edad = DatosEdad._20
        datos_edad.valor = sline[24]
        datos_edad.sexo = DatosEdad.MUJER
        datos_edad.datos_paro = datos_paro
        datos_edad.save()
        datos_edad = DatosEdad()
        datos_edad.edad = DatosEdad._20_24
        datos_edad.valor = sline[25]
        datos_edad.sexo = DatosEdad.MUJER
        datos_edad.datos_paro = datos_paro
        datos_edad.save()
        datos_edad = DatosEdad()
        datos_edad.edad = DatosEdad._25_29
        datos_edad.valor = sline[26]
        datos_edad.sexo = DatosEdad.MUJER
        datos_edad.datos_paro = datos_paro
        datos_edad.save()
        datos_edad = DatosEdad()
        datos_edad.edad = DatosEdad._30_34
        datos_edad.valor = sline[27]
        datos_edad.sexo = DatosEdad.MUJER
        datos_edad.datos_paro = datos_paro
        datos_edad.save()
        datos_edad = DatosEdad()
        datos_edad.edad = DatosEdad._35_39
        datos_edad.valor = sline[28]
        datos_edad.sexo = DatosEdad.MUJER
        datos_edad.datos_paro = datos_paro
        datos_edad.save()
        datos_edad = DatosEdad()
        datos_edad.edad = DatosEdad._40_44
        datos_edad.valor = sline[29]
        datos_edad.sexo = DatosEdad.MUJER
        datos_edad.datos_paro = datos_paro
        datos_edad.save()
        datos_edad = DatosEdad()
        datos_edad.edad = DatosEdad._45_49
        datos_edad.valor = sline[30]
        datos_edad.sexo = DatosEdad.MUJER
        datos_edad.datos_paro = datos_paro
        datos_edad.save()
        datos_edad = DatosEdad()
        datos_edad.edad = DatosEdad._50_54
        datos_edad.valor = sline[31]
        datos_edad.sexo = DatosEdad.MUJER
        datos_edad.datos_paro = datos_paro
        datos_edad.save()
        datos_edad = DatosEdad()
        datos_edad.edad = DatosEdad._55_59
        datos_edad.valor = sline[32]
        datos_edad.sexo = DatosEdad.MUJER
        datos_edad.datos_paro = datos_paro
        datos_edad.save()
        datos_edad = DatosEdad()
        datos_edad.edad = DatosEdad._59
        datos_edad.valor = sline[33]
        datos_edad.sexo = DatosEdad.MUJER
        datos_edad.datos_paro = datos_paro
        datos_edad.save()
        #Estudios
        datos_estudios = DatosEstudios()
        datos_estudios.estudios = datos_estudios.SIN_ALFABETIZAR
        datos_estudios.valor = sline[35]
        datos_estudios.datos_paro = datos_paro
        datos_estudios.save()
        datos_estudios = DatosEstudios()
        datos_estudios.estudios = datos_estudios.ESTUDIOS_PRIMARIOS
        datos_estudios.valor = sline[36]
        datos_estudios.datos_paro = datos_paro
        datos_estudios.save()
        datos_estudios = DatosEstudios()
        datos_estudios.estudios = datos_estudios.CERTIFICADO_ESCOLAR
        datos_estudios.valor = sline[37]
        datos_estudios.datos_paro = datos_paro
        datos_estudios.save()
        datos_estudios = DatosEstudios()
        datos_estudios.estudios = datos_estudios.ESO
        datos_estudios.valor = sline[38]
        datos_estudios.datos_paro = datos_paro
        datos_estudios.save()
        datos_estudios = DatosEstudios()
        datos_estudios.estudios = datos_estudios.EGB
        datos_estudios.valor = sline[39]
        datos_estudios.datos_paro = datos_paro
        datos_estudios.save()
        datos_estudios = DatosEstudios()
        datos_estudios.estudios = datos_estudios.BACHILLER
        datos_estudios.valor = sline[40]
        datos_estudios.datos_paro = datos_paro
        datos_estudios.save()
        datos_estudios = DatosEstudios()
        datos_estudios.estudios = datos_estudios.FP
        datos_estudios.valor = sline[41]
        datos_estudios.datos_paro = datos_paro
        datos_estudios.save()
        datos_estudios = DatosEstudios()
        datos_estudios.estudios = datos_estudios.GRADO_MEDIO
        datos_estudios.valor = sline[42]
        datos_estudios.datos_paro = datos_paro
        datos_estudios.save()
        datos_estudios = DatosEstudios()
        datos_estudios.estudios = datos_estudios.GRADO_SUPERIOR
        datos_estudios.valor = sline[43]
        datos_estudios.datos_paro = datos_paro
        datos_estudios.save()
        datos_estudios = DatosEstudios()
        datos_estudios.estudios = datos_estudios.OTROS
        datos_estudios.valor = sline[44]
        datos_estudios.datos_paro = datos_paro
        datos_estudios.save()
        print 'Procesada(s) %s fila(s)' % count
        sys.stdout.flush()
        count += 1

f.close()
print 'Finished!'
