# -*- coding: utf-8 -*-
import csv

TotalAraucania=0

with open('CasosNuevosCumulativo.csv','r') as datos:
    diccionario = csv.DictReader(datos)
    headers=diccionario.fieldnames
    #print(headers)
    for dia in diccionario:
        if dia['Region']=="Los Lagos":
            for fecha in headers[1:]:
                print(fecha)
                TotalAraucania=TotalAraucania+float(dia[fecha])            
print('El total de casos en la region de Los lagos es: '+str(TotalAraucania))
