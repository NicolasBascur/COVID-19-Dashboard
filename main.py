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

totales_csv = '.\\datos_ordernar\\regiones\\TotalesPorRegion.csv'
fallecidos_csv = '.\\datos_ordernar\\regiones\\FallecidosCumulativo.csv'
reg_acumulativo_csv = '.\\datos_ordernar\\regiones\\CasosNuevosCumulativo.csv'


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

    opcion_mat_reg = st.selectbox(
                            'Metrica a observar: ',
                         ('Totales', 'CasosNuevosAcumulativos', 'Fallecidos'))

    if opcion_mat_reg == "Totales":
        regtotal = ld.datosRegionTotales(totales_csv, valor_reg)
        regtotal = ld.datosRegionTotales_grafico(regtotal)
        #st.write(regtotal)
        st.line_chart(data=regtotal.reset_index(drop=True), use_container_width=True)

    if opcion_mat_reg == "CasosNuevosAcumulativos":
        regtotal = ld.datosRegionAcumulativos(reg_acumulativo_csv, valor_reg)
        #st.write(regtotal)
        st.line_chart(data=regtotal.reset_index(drop=True), use_container_width=True)

    if opcion_mat_reg == "Fallecidos":
        regtotal = ld.datosRegionFallecidos(fallecidos_csv, valor_reg)
        #st.write(regtotal)
        st.line_chart(data=regtotal.reset_index(drop=True), use_container_width=True)

    st.write('Datos procesados de la region '+ valor_reg +'', tabla_muestra[['Fecha', 'Confirmados','Recuperados','Muertes']])
    ##st.pyplot(cs.line_plot(total_df[["Infected", "Fatal", "Recovered"]], "Total number of cases over time"))


    "Sir"
    st.pyplot(plt)
    

#MATRICES COMUNAS --------------------------------------------------------------------------------------------------------------
elif radio == "Comuna":
    valor_com=st.sidebar.selectbox('Seleccione region:',ld.comunas)