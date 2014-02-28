from django.db import models

# Create your models here.

class Provincia(models.Model):
    nombre = models.CharField(max_length=20)
    codigo = models.IntegerField()
    
class Comarca(models.Model):
    nombre = models.CharField(max_length=20)
    codigo = models.IntegerField()
    provincia = models.ForeignKey(Provincia)
    
class Municipio(models.Model):
    nombre = models.CharField(max_length=20)
    codigo = models.IntegerField()
    comarca = models.ForeignKey(Comarca)

class DatosParo(models.Model):
    municipio = models.ForeignKey(Municipio)
    poblacion_total = models.IntegerField()
    poblacion_activa = models.IntegerField()
    parados = models.IntegerField()
    ano = models.IntegerField()
    trimestre = models.IntegerField()

class DatosEdad(models.Model):
    _20 = '<20'
    _20_24 = '20-24'
    _25_29 = '25-29'
    _30_34 = '30-34'
    _35_39 = '35-39'
    _40_44 = '40-44'
    _45_49 = '45-49'
    _50_54 = '50-54'
    _55_59 = '55-59'
    _59 = '>59'
    EDAD_CHOICES = (
        (_20, '<20'),
        (_20_24, '20-24'),
        (_25_29, '25-29'),
        (_30_34, '30-34'),
        (_35_39, '35-39'),
        (_40_44, '40-44'),
        (_45_49, '45-49'),
        (_50_54, '50-54'),
        (_55_59, '55-59'),
        (_59, '>59'),
    )
    edad = models.CharField(max_length=20, choices=EDAD_CHOICES)
    valor = models.IntegerField()
    HOMBRE = 'H'
    MUJER = 'M'
    SEXO_CHOICES = (
        (HOMBRE, 'Hombre'), 
        (MUJER, 'Mujer'),
    )
    sexo = models.CharField(max_length=2, choices=SEXO_CHOICES)
    datos_paro = models.ForeignKey(DatosParo)
    
class DatosEstudios(models.Model):
    SIN_ALFABETIZAR = 'SIN_ALFABETIZAR'
    ESTUDIOS_PRIMARIOS = 'ESTUDIOS_PRIMARIOS'
    CERTIFICADO_ESCOLAR = 'CERTIFICADO_ESCOLAR'
    ESO = 'ESO'
    EGB = 'EGB'
    BACHILLER = 'BACHILLER'
    FP = 'FP'
    GRADO_MEDIO = 'GRADO_MEDIO'
    GRADO_SUPERIOR = 'GRADO_SUPERIOR'
    OTROS = 'OTROS'    
    ESTUDIOS_CHOICES = (
        (SIN_ALFABETIZAR, 'Sin alfabetizar'),
        (ESTUDIOS_PRIMARIOS, 'Estudios primarios'),
        (CERTIFICADO_ESCOLAR, 'Certificado escolar'),
        (ESO, 'ESO'),
        (EGB, 'EGB'),
        (BACHILLER, 'Bachiller'),
        (FP, 'FP'),
        (GRADO_MEDIO, 'Gradio medio'),
        (GRADO_SUPERIOR, 'Grado Superior'),
        (OTROS, 'Otros'),
    )
    estudios = models.CharField(max_length=20, choices=ESTUDIOS_CHOICES)  
    valor = models.IntegerField()
    datos_paro = models.ForeignKey(DatosParo)
