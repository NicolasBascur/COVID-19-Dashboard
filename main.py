import leer_data # Nuestra libreria de funciones. 
import streamlit as st # programa para modelar los datos.
import numpy as np 
import pandas as pd # dataframe/set

####Directorio de los archivos
casosTotalesCumulativoRegion = "datos/CasosTotalesCumulativo_T.csv"
muertesTotalesCumulativasRegion = "datos/FallecidosCumulativo_T.csv"
#caso sintoma Region
nuevoSintomasRegion = "datos/CasosNuevosConSintomas_T.csv"
casosTotalRegion = "datos/2020-10-25-CasosConfirmados-totalRegional.csv"
casosTotalRegiones = "datos/2020-10-27-CasosConfirmados-totalRegional.csv"
###
#

st.title("Covid19 Dashboard Chile - 2020")
st.write("Aqui vamos a ver el progreso diario del covid19 de cada region")

opcionRegion = st.selectbox("Seleccionar region",leer_data.regiones)
st.write("Seleccionaste", opcionRegion)

#### Camabiar esto para que las funciones devuelvan un data frame panda en vez de los datos. 
cRegion = leer_data.datosRegionCumulativo(casosTotalesCumulativoRegion,opcionRegion)# casos Dias cumulativos por region
mRegion = leer_data.datosRegionCumulativo(muertesTotalesCumulativasRegion,opcionRegion) # muertos dias cumulativoss por region
sRegion = leer_data.datosRegionCumulativo(nuevoSintomasRegion,opcionRegion) # casos nuevos con sintomas 
ctRegion = leer_data.datosRegionTotales(casosTotalRegion,opcionRegion) #Casos totales por Region, una sola region
ctRegiones = leer_data.casosRegionesTotales(casosTotalRegiones) # casos totales de toda la region
###

# 2 formas de escribir la tabla de datos
st.write("horizontal")
st.write(pd.DataFrame({ # streamlit sabe lo que es un dataset y lo interpreta y lo escribe
    'Fecha':cRegion[0],
    'Casos':cRegion[1]
}))

st.write("vertical")
st.write(pd.DataFrame( 
    [cRegion[1]],
    columns=cRegion[0]
))

"Grafica"
# dataframe de la grafica
# cRegion 1 es cantidad de casos, cRegion 0 la fecha
grafica= pd.DataFrame(cRegion[1],cRegion[0])
st.line_chart(grafica,use_container_width=False) # dibujamos la grafica , jugar con los parametros

st.write("Muertos Covid")

st.write("horizontal")
st.write(pd.DataFrame({
    'Fecha':mRegion[0],
    'Casos':mRegion[1]
}))

st.write("vertical")
st.write(pd.DataFrame(
    [mRegion[1]],
    columns=mRegion[0]
))

"Grafica"
grafica= pd.DataFrame(mRegion[1],mRegion[0])
st.line_chart(grafica)

"Casos Totales Region"
# hacer que la funcion para leer datos devuelva el dataframe de panda.
#
#casos total Regiones: 
print(ctRegiones)
st.write(pd.DataFrame(ctRegiones[1][0:-1],ctRegiones[0][0:-1]))#un poco de manipulacion de index para saltarme los datos que no quiero

st.bar_chart(pd.DataFrame(ctRegiones[1][0:-2],ctRegiones[0][0:-2]))

