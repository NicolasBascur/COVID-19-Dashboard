import leer_data # Nuestra libreria de funciones. 
import streamlit as st # programa para modelar los datos.
import numpy as np
import pandas as pd
import SessionState #Libreria que permite paginacion





#Paginacion Sidebar
st.sidebar.title("Paginas")
radio = st.sidebar.radio(label="", options=["Region", "Comuna"])
session_state = SessionState.get(a=0, b=0) 
st.title("Covid19 Dashboard Chile - 2020")



#MATRICES REGIONES --------------------------------------------------------------------------------------------------------------
if radio == "Region":

    ####Archivos
    ####
    ctcRegion = "./datos/regiones/CasosTotalesCumulativo_T.csv"
    mtcRegion = "./datos/regiones/FallecidosCumulativo_T.csv"
    #caso sintoma Region
    csRegion = "./datos/regiones/CasosNuevosConSintomas_T.csv"
    ctRegion = "./datos/regiones/2020-10-25-CasosConfirmados-totalRegional.csv"
    ###
    #
    
    st.write("Aqui vamos a ver el progreso diario del covid19 de cada region")

    opcionRegion = st.selectbox("Seleccionar region",leer_data.regiones)
    st.write("Seleccionaste", opcionRegion)

    cRegion = leer_data.datosRegionCumulativo(ctcRegion,opcionRegion)
    mRegion = leer_data.datosRegionCumulativo(mtcRegion,opcionRegion) 
    sRegion = leer_data.datosRegionCumulativo(csRegion,opcionRegion)
    ctRegion = leer_data.datosRegionTotales(ctRegion,opcionRegion)

    st.write("horizontal")
    st.write(pd.DataFrame({
        'Fecha':cRegion[0],
        'Casos':cRegion[1]
    }))

    st.write("vertical")
    st.write(pd.DataFrame(
        [cRegion[1]],
        columns=cRegion[0]
    ))
    "Grafica"

    grafica= pd.DataFrame(cRegion[1],cRegion[0])
    st.line_chart(grafica)

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

    print(ctRegion)
    st.write(pd.DataFrame.from_records(ctRegion,index=[0]))


#MATRICES COMUNAS --------------------------------------------------------------------------------------------------------------
elif radio == "Comuna":

    ctcComuna = "./datos/comunas/Covid-19.csv"
    st.write("Aqui vamos a ver el progreso diario del covid19 de cada comuna")
    opcionComuna = st.selectbox("Seleccionar Comuna",leer_data.comunas)
    st.write("Comuna seleccionada: ", opcionComuna)
    cComuna = leer_data.datosComunaCumulativo(ctcComuna ,opcionComuna)
    st.write("#Histograma casos contagios acumulativos")
    st.dataframe(cComuna)
    st.bar_chart(cComuna)

