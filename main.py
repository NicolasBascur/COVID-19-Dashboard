import os
import pprint
import pandas as pd
import datetime
import streamlit as st
import covsirphy as cs
import SessionState
import texto
data_loader = cs.DataLoader("csv")
csvregion = pd.read_csv("csv/covid19dh.csv")
CHL = csvregion.loc[csvregion["ISO3"]=='CHL']
CHL.to_csv('./csv/region.csv') 

# The number of cases (JHU style)
#jhu_data = data_loader.jhu(verbose=True)
## Population in each country
#population_data = data_loader.population(verbose=True)
## Government Response Tracker (OxCGRT)
#oxcgrt_data = data_loader.oxcgrt(verbose=True)
#jhu_data.subset("Japan", province="Tokyo").tail()


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
    table_reg = pd.read_csv("./csv/region.csv")
    table_reg= table_reg.rename(columns={'ObservationDate': 'Fecha', 'Confirmed':'Confirmados', 'Recovered':'Recuperados', 'Deaths':'Muertes','Population':'Poblacion','Province/State':'Region'})
    st.markdown("Datos ")
    #Valor de region, nombre
    valor_reg=st.sidebar.selectbox('Seleccione region:',
                        ("Arica y Parinacota","Tarapacá","Antofagasta","Atacama","Coquimbo","Valparaíso","Metropolitana","O’Higgins","Maule","Ñuble","Biobío","Araucanía","Los Ríos","Los Lagos","Aysén","Magallanes")
                        )
    #Valor de fecha inicial
    
    valor_fechai = st.sidebar.date_input("Fecha Inicial", datetime.date(2020, 11, 6))
    tabla_muestra= table_reg.loc[(table_reg['Region'] == valor_reg)]
    st.write('Datos de la region '+ valor_reg +'', tabla_muestra[['Fecha', 'Poblacion','Confirmados','Recuperados','Muertes']], 'Above is a dataframe.')




elif radio == "Comuna":
    st.markdown("Comunas")