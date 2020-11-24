import os
import pprint
import pandas as pd
import SessionState
import leer_data as ld#Libreria que permite paginacion
from  sir import plt
import datetime
import streamlit as st
import covsirphy as cs
import altair as alt
import SessionState
import texto
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


#Se crea csv principal donde se realizara la prediccion
#data_loader = cs.DataLoader("csv_listo")
csvregion = pd.read_csv("csv_listo/covid19dh.csv")
CHL = csvregion.loc[csvregion["ISO3"]=='CHL']
CHL.to_csv('./csv_listo/region.csv') 

#CSV para mostrar diferentes metricas
#CSV REGIONES
totales_csv = '.\\datos_ordernar\\regiones\\TotalesPorRegion.csv'
fallecidos_csv = '.\\datos_ordernar\\regiones\\FallecidosCumulativo.csv'
reg_acumulativo_csv = '.\\datos_ordernar\\regiones\\CasosNuevosCumulativo.csv'
#CSV COMUNAS
total_com = '.\\datos_ordernar\\comunas\\Covid-19.csv'
activos_com = '.\\datos_ordernar\\comunas\\CasosActivosPorComuna.csv'
confirmados_com = '.\\datos_ordernar\\comunas\\CasosConfirmadosPorComuna.csv'
fallecidos_com = '.\\datos_ordernar\\comunas\\CasosFallecidosPorComuna.csv'
#
##jhu_data = data_loader.jhu(verbose=True)
# Population in each country
##population_data = data_loader.population(verbose=True)
# Government Response Tracker (OxCGRT)
##oxcgrt_data = data_loader.oxcgrt(verbose=True)
#




#Paginacion Sidebar
st.sidebar.title("Paginas")
st.title("Covid19 Dashboard Chile - 2020")
st.markdown("## Modelo Epidemiológico SIR")
st.sidebar.markdown(texto.PARAMETER_SELECTION)
radio = st.sidebar.radio(label="", options=["Region", "Comuna"])
session_state = SessionState.get(a=0, b=0) 
st.markdown(texto.MODEL_INTRO)
#MATRICES REGIONES --------------------------------------------------------------------------------------------------------------
if radio == "Region":

    table_reg = pd.read_csv("./csv_listo/region.csv")
    table_reg= table_reg.rename(columns={'ObservationDate': 'Fecha', 'Confirmed':'Confirmados', 'Recovered':'Recuperados', 'Deaths':'Muertes','Population':'Poblacion','Province/State':'Region'})
    st.markdown("Datos ")
    #Valor de region, nombre
    valor_reg=st.sidebar.selectbox('Seleccione region:',ld.regiones)
    valor_fechai = st.sidebar.date_input("Fecha Inicial", datetime.date(2020, 3, 22))
    valor_fechai = st.sidebar.date_input("Fecha Final", datetime.date(2020, 11, 6))
    tabla_muestra= table_reg.loc[(table_reg['Region'] == valor_reg)]
    opcion_mat_reg = st.selectbox('Metrica a observar: ', ld.metricasreg)
    if opcion_mat_reg == "Totales":
        regtotal = ld.datosRegionTotales(totales_csv, valor_reg)
        regtotal = ld.datosRegionTotales_grafico(regtotal)
        #st.write(regtotal)
        st.write('Dias/Personas')
        st.line_chart(data=regtotal.reset_index(drop=True), use_container_width=True)

    if opcion_mat_reg == "Casos Nuevos Acumulativos":
        regtotal = ld.datosRegionAcumulativos(reg_acumulativo_csv, valor_reg)
        #st.write(regtotal)
        st.write('Dias/Personas')
        st.line_chart(data=regtotal.reset_index(drop=True), use_container_width=True)

    if opcion_mat_reg == "Fallecidos":
        regtotal = ld.datosRegionFallecidos(fallecidos_csv, valor_reg)
        #st.write(regtotal)
        st.write('Dias/Personas')
        st.line_chart(data=regtotal.reset_index(drop=True), use_container_width=True)

    st.write('Datos procesados de la region '+ valor_reg +'', tabla_muestra[['Fecha', 'Confirmados','Recuperados','Muertes']])
    ##st.pyplot(cs.line_plot(total_df[["Infected", "Fatal", "Recovered"]], "Total number of cases over time"))


    "Sir"
    st.pyplot(plt)
    

#MATRICES COMUNAS --------------------------------------------------------------------------------------------------------------
elif radio == "Comuna":
    st.markdown("Datos ")
    valor_com=st.sidebar.selectbox('Seleccione region:',ld.comunas)
    valor_fechai = st.sidebar.date_input("Fecha Inicial", datetime.date(2020, 3, 22))
    valor_fechai = st.sidebar.date_input("Fecha Final", datetime.date(2020, 11, 6))
    opcion_mat_com = st.selectbox('Metrica a observar: ', ld.metricascom)
    if opcion_mat_com == "Total contagiados":
        comval, pob = ld.datosComunasTotales(total_com, valor_com)
        st.write('La poblacion total de '+ str(valor_com) +' es de: ' + str(pob)+'.   Intervalos de dos dias/Personas')
        st.line_chart(data=comval.reset_index(drop=True), use_container_width=True)

    if opcion_mat_com == "Casos activos":
        comval, pob = ld.datosComunasActivos(activos_com, valor_com)
        st.write('La poblacion total de '+ str(valor_com) +' es de: ' + str(pob)+'.     Intervalos de dos a tres dias/Personas')
        st.line_chart(data=comval.reset_index(drop=True), use_container_width=True)

    if opcion_mat_com == "Casos confirmados":
        comval, pob = ld.datosComunasConfirmados(confirmados_com, valor_com)
        st.write('La poblacion total de '+ str(valor_com) +' es de: ' + str(pob)+'.     Intervalos de dos a cinco dias/Personas')
        st.line_chart(data=comval.reset_index(drop=True), use_container_width=True)

    if opcion_mat_com == "Fallecidos":
        comval, pob = ld.datosComunasFallecidos(fallecidos_com, valor_com)
        st.write('La poblacion total de '+ str(valor_com) +' es de: ' + str(pob)+'.     Intervalos de dos a cinco dias/Personas')
        st.line_chart(data=comval.reset_index(drop=True), use_container_width=True)