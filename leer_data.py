# -*- coding: utf-8 -*-

import csv
#Lista con todas las regiones
regiones = ["Arica y Parinacota","Tarapacá","Antofagasta","Atacama","Coquimbo","Valparaíso","Metropolitana"\
    ,"O’Higgins","Maule","Ñuble","Biobío","Araucanía","Los Ríos","Los Lagos","Aysén","Magallanes"]
#total casos diarios Region
#tcdR =  "datos/TotalesPorRegion.csv"
#casosTotalesCumulativosRegion
#ctcRegion = "datos/CasosTotalesCumulativo_T.csv"
#
# Implementar panda para cargar los archivos csv
#
def datosRegionCumulativo(archivo,region): #directorio archivo , Nombre de region a buscar.
    tcasos= [[],[]]
    with open(archivo,'r',encoding='utf-8') as cvs:
        diccionario = csv.DictReader(cvs)
        # headers=diccionario.fieldnames
        #print(region)
        for datos in diccionario:
            tcasos[0].append(datos['Region'])
            tcasos[1].append(int(float(datos[region])))
    return tcasos

def datosRegionTotales(archivo,region):
    with open(archivo,'r',encoding='utf-8') as cvs:
        diccionario = csv.DictReader(cvs)
        for datos in diccionario:
            if(datos['Region']==region):
                return(datos)
            
    

def leerRegionDiario():
    #LEEER TODOS LOS archivos de la carpeta
    return 

def leerOtrosDatosRegion():
    return

