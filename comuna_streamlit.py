import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# URL de Archivo debe esta en estado RAW para ser analizado.
DATA_URL = ("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto1/Covid-19.csv")
 

def load_data():
    data = pd.read_csv(DATA_URL)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

#Titulo
st.write("""
#Comunas 


Casos totales por comuna incremental
""")



data = load_data()
st.dataframe(data)