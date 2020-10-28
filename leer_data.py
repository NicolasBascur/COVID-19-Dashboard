# -*- coding: utf-8 -*-
import csv
#import pandas as pd
# Implementar panda para cargar los archivos csv y crear los datasets directamente????

def datosRegionCumulativo(archivo,region): #directorio archivo , Nombre de region a buscar.
    tcasos= [[],[]] # es una lista con 2 arreglos. [Nombre Region][Cantidad de casos] en retroespectiva, podria haberlos hecho pareja
    with open(archivo,'r',encoding='utf-8') as cvs:# Abrimos el archivo 
        diccionario = csv.DictReader(cvs) #cargamos el archivo csv como un diccionario
        # headers=diccionario.fieldnames
        #print(region)
        for datos in diccionario: # Actualmente solo necesitaba el nombre de la region y el numero de casos
            tcasos[0].append(datos['Region'])
            tcasos[1].append(int(float(datos[region])))
    return tcasos

def datosRegionTotales(archivo,region='all'):
    with open(archivo,'r',encoding='utf-8') as cvs:
        diccionario = csv.DictReader(cvs)
        for datos in diccionario:
            if(datos['Region']==region):
                return(datos)
            

def casosRegionesTotales(archivo):
    totalRegiones=[[],[]]
    with open(archivo,'r',encoding='utf-8') as cvs:
        diccionario = csv.DictReader(cvs)
        for datos in diccionario:
            totalRegiones[0].append(datos['Region'])
            totalRegiones[1].append(int(datos['Casos totales acumulados']))
            #totalRegiones.append(datos)#devuelve el diccionario con todas las regiones
    return totalRegiones        

def leerRegionDiario():
    #LEEER TODOS LOS archivos de la carpeta
    return 

def leerOtrosDatosRegion():
    return

