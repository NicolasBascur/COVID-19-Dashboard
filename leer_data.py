# -*- coding: utf-8 -*-
import pandas as pd
#Lista con todas las regiones
regiones = ["Arica y Parinacota","Tarapacá","Antofagasta","Atacama","Coquimbo","Valparaíso","Metropolitana","O’Higgins","Maule","Ñuble","Biobío","Araucanía","Los Ríos","Los Lagos","Aysén","Magallanes"]
#Lista de comunas
comunas=["Arica","Camarones","General Lagos","Putre","Desconocido Arica y Parinacota","Alto Hospicio","Camina","Colchane","Huara","Iquique","Pica","Pozo Almonte","Desconocido Tarapaca","Antofagasta","Calama","Maria Elena","Mejillones","Ollague","San Pedro de Atacama","Sierra Gorda","Taltal","Tocopilla","Desconocido Antofagasta","Alto del Carmen","Caldera","Chanaral","Copiapo","Diego de Almagro","Freirina","Huasco","Tierra Amarilla","Vallenar","Desconocido Atacama","Andacollo","Canela","Combarbala","Coquimbo","Illapel","La Higuera","La Serena","Los Vilos","Monte Patria","Ovalle","Paiguano","Punitaqui","Rio Hurtado","Salamanca","Vicuna","Desconocido Coquimbo","Algarrobo","Cabildo","Calera","Calle Larga","Cartagena","Casablanca","Catemu","Concon","El Quisco","El Tabo","Hijuelas","Isla de Pascua","Juan Fernandez","La Cruz","La Ligua","Limache","Llaillay","Los Andes","Nogales","Olmue","Panquehue","Papudo","Petorca","Puchuncavi","Putaendo","Quillota","Quilpue","Quintero","Rinconada","San Antonio","San Esteban","San Felipe","Santa Maria","Santo Domingo","Valparaiso","Villa Alemana","Vina del Mar","Zapallar","Desconocido Valparaiso","Alhue","Buin","Calera de Tango","Cerrillos","Cerro Navia","Colina","Conchali","Curacavi","El Bosque","El Monte","Estacion Central","Huechuraba","Independencia","Isla de Maipo","La Cisterna","La Florida","La Granja","La Pintana","La Reina","Lampa","Las Condes","Lo Barnechea","Lo Espejo","Lo Prado","Macul","Maipu","Maria Pinto","Melipilla","Nunoa","Padre Hurtado","Paine","Pedro Aguirre Cerda","Penaflor","Penalolen","Pirque","Providencia","Pudahuel","Puente Alto","Quilicura","Quinta Normal","Recoleta","Renca","San Bernardo","San Joaquin","San Jose de Maipo","San Miguel","San Pedro","San Ramon","Santiago","Talagante","Tiltil","Vitacura","Desconocido Metropolitana","Chepica","Chimbarongo","Codegua","Coinco","Coltauco","Donihue","Graneros","La Estrella","Las Cabras","Litueche","Lolol","Machali","Malloa","Marchihue","Mostazal","Nancagua","Navidad","Olivar","Palmilla","Paredones","Peralillo","Peumo","Pichidegua","Pichilemu","Placilla","Pumanque","Quinta de Tilcoco","Rancagua","Rengo","Requinoa","San Fernando","San Vicente","Santa Cruz","Desconocido Oâ€™Higgins","Cauquenes","Chanco","Colbun","Constitucion","Curepto","Curico","Empedrado","Hualane","Licanten","Linares","Longavi","Maule","Molina","Parral","Pelarco","Pelluhue","Pencahue","Rauco","Retiro","Rio Claro","Romeral","Sagrada Familia","San Clemente","San Javier","San Rafael","Talca","Teno","Vichuquen","Villa Alegre","Yerbas Buenas","Desconocido Maule","Bulnes","Chillan","Chillan Viejo","Cobquecura","Coelemu","Coihueco","El Carmen","Ninhue","Niquen","Pemuco","Pinto","Portezuelo","Quillon","Quirihue","Ranquil","San Carlos","San Fabian","San Ignacio","San Nicolas","Treguaco","Yungay","Desconocido Nuble","Alto Biobio","Antuco","Arauco","Cabrero","Canete","Chiguayante","Concepcion","Contulmo","Coronel","Curanilahue","Florida","Hualpen","Hualqui","Laja","Lebu","Los Alamos","Los Angeles","Lota","Mulchen","Nacimiento","Negrete","Penco","Quilaco","Quilleco","San Pedro de la Paz","San Rosendo","Santa Barbara","Santa Juana","Talcahuano","Tirua","Tome","Tucapel","Yumbel","Desconocido Biobio","Angol","Carahue","Cholchol","Collipulli","Cunco","Curacautin","Curarrehue","Ercilla","Freire","Galvarino","Gorbea","Lautaro","Loncoche","Lonquimay","Los Sauces","Lumaco","Melipeuco","Nueva Imperial","Padre Las Casas","Perquenco","Pitrufquen","Pucon","Puren","Renaico","Saavedra","Temuco","Teodoro Schmidt","Tolten","Traiguen","Victoria","Vilcun","Villarrica","Desconocido Araucania","Corral","Futrono","La Union","Lago Ranco","Lanco","Los Lagos","Mafil","Mariquina","Paillaco","Panguipulli","Rio Bueno","Valdivia","Desconocido Los Rios","Ancud","Calbuco","Castro","Chaiten","Chonchi","Cochamo","Curaco de Velez","Dalcahue","Fresia","Frutillar","Futaleufu","Hualaihue","Llanquihue","Los Muermos","Maullin","Osorno","Palena","Puerto Montt","Puerto Octay","Puerto Varas","Puqueldon","Purranque","Puyehue","Queilen","Quellon","Quemchi","Quinchao","Rio Negro","San Juan de la Costa","San Pablo","Desconocido Los Lagos","Aysen","Chile Chico","Cisnes","Cochrane","Coyhaique","Guaitecas","Lago Verde","OHiggins","Rio Ibanez","Tortel","Desconocido Aysen","Antartica","Cabo de Hornos","Laguna Blanca","Natales","Porvenir","Primavera","Punta Arenas","Rio Verde","San Gregorio","Timaukel","Torres del Paine","Desconocido Magallanes"]

metricasreg=['Totales', 'Casos Nuevos Acumulativos', 'Fallecidos']
metricascom=['Total contagiados', 'Casos activos', 'Casos confirmados', 'Fallecidos']



#MATRICES REGION


def datosRegionTotales(archivo, region):
    data = pd.read_csv(archivo)
    data = data.loc[data['Region'] == region]
    #data = (data[data.columns[5:-1]]).T
    return data

def datosRegionAcumulativos(archivo, region):
    data = pd.read_csv(archivo)
    data = data.loc[data['Region'] == region]
    data = data.transpose()
    data = data.rename(columns={0: 'Casos nuevos'})
    return data

def datosRegionFallecidos(archivo, region):
    data = pd.read_csv(archivo)
    data = data.loc[data['Region'] == region]
    data = data.transpose()
    data = data.rename(columns={0: 'Fallecidos'})
    return data

def datosRegionTotales_grafico(regtotal):
    regtotal = regtotal.drop('Region',axis=1)
    regtotal = regtotal.transpose()
    regtotal = regtotal.drop(['Categoria'])
    for x in range(17):
        regtotal = regtotal.rename(columns={0+x: 'Casos acumulados'
                                            , 17+x:'Casos nuevos totales'
                                            , 34+x:'Casos nuevos con sintomas'
                                            , 51+x:'Casos nuevos sin sintomas'
                                            , 68+x:'Casos nuevos sin notificar'
                                            , 85+x:'Fallecidos totales'
                                            , 102+x:'Casos confirmados recuperados'
                                            , 119+x:'Casos activos confirmados'
                                            , 136+x:'Casos activos probables'
                                            , 153+x:'Casos probables acumulados'})
    return regtotal



#MATRICES COMUNAS

#Las funciones son las mismas pero por las dudas las mantedre en caso de tener que agregar un cambio por separado

def datosComunasTotales(archivo,comtotal): #directorio archivo , Nombre de comuna a buscar
    data = pd.read_csv(archivo)
    data = data.loc[data['Comuna'] == comtotal]
    val  = data['Poblacion'].values[0]
    data = data.drop(columns=['Region', 'Codigo region', 'Poblacion','Tasa','Comuna','Codigo comuna'])
    data = data.transpose()
    data = data.rename(columns={0: 'Total contagios'})
    return data, val

def datosComunasActivos(archivo,comtotal): #directorio archivo , Nombre de comuna a buscar
    data = pd.read_csv(archivo)
    data = data.loc[data['Comuna'] == comtotal]
    val  = data['Poblacion'].values[0]
    data = data.drop(columns=['Region', 'Codigo region', 'Poblacion','Comuna','Codigo comuna'])
    data = data.transpose()
    data = data.rename(columns={0: 'Casos activos'})
    return data, val

def datosComunasConfirmados(archivo,comtotal): #directorio archivo , Nombre de comuna a buscar
    data = pd.read_csv(archivo)
    data = data.loc[data['Comuna'] == comtotal]
    val  = data['Poblacion'].values[0]
    data = data.drop(columns=['Region', 'Codigo region', 'Poblacion','Comuna','Codigo comuna'])
    data = data.transpose()
    data = data.rename(columns={43: 'Casos Confirmados'})
    return data, val

def datosComunasFallecidos(archivo,comtotal): #directorio archivo , Nombre de comuna a buscar
    data = pd.read_csv(archivo)
    data = data.loc[data['Comuna'] == comtotal]
    val  = data['Poblacion'].values[0]
    data = data.drop(columns=['Region', 'Codigo region', 'Poblacion','Comuna','Codigo comuna'])
    data = data.transpose()
    data = data.rename(columns={43: 'Defunciones'})
    return data, val