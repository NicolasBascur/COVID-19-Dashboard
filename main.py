import os
import pprint
import pandas as pd
import SessionState #Libreria que permite paginacion
# from  sir import plt
import datetime
import streamlit as st
import covsirphy as cs
import SessionState
import texto
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
data_loader = cs.DataLoader("csv_listo")
csvregion = pd.read_csv("csv_listo/covid19dh.csv")
CHL = csvregion.loc[csvregion["ISO3"]=='CHL']
CHL.to_csv('./csv_listo/region.csv') 

jhu_data = data_loader.jhu(verbose=True)
# Population in each country
population_data = data_loader.population(verbose=True)
# Government Response Tracker (OxCGRT)
oxcgrt_data = data_loader.oxcgrt(verbose=True)





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
    valor_reg=st.sidebar.selectbox('Seleccione region:',
                        ("Arica y Parinacota","Tarapacá","Antofagasta","Atacama","Coquimbo","Valparaíso","Metropolitana","O’Higgins","Maule","Ñuble","Biobío","Araucanía","Los Ríos","Los Lagos","Aysén","Magallanes")
                        )
    #Valor de fecha inicial
    
    valor_fechai = st.sidebar.date_input("Fecha Inicial", datetime.date(2020, 11, 6))
    tabla_muestra= table_reg.loc[(table_reg['Region'] == valor_reg)]
    jhu_data.subset("Chile", province=valor_reg).tail()
    total_df = jhu_data.total()
    total_df.tail()



    st.write('Datos de la region '+ valor_reg +'', tabla_muestra[['Fecha', 'Poblacion','Confirmados','Recuperados','Muertes']], 'Above is a dataframe.')
    st.pyplot(cs.line_plot(total_df[["Infected", "Fatal", "Recovered"]], "Total number of cases over time"))


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


    "Sir"
    st.pyplot(plt)
    

#MATRICES COMUNAS --------------------------------------------------------------------------------------------------------------
elif radio == "Comuna":
    st.markdown("Comunas")