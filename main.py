# ---- Librerias ----
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import plotly.express as px
from io import StringIO
import pandas as pd
import seaborn as sns


# ---- Carga del archivo y preprocesamiento ----
# st.set_page_config(page_title="USO DE DROGAS Y FACTORES DE RIESGO ASOCIADOS", layout="centered", page_icon="💊")

import contexto_Historico,EDA_Consumo,EDA_Adictos,Simulaciones_pag4,Predicción



class MultiApp:
    
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        
        # app = st.sidebar(
        
        with st.sidebar:
            st.image("img/marihuana-01.png",width=300)        
            app = option_menu(
                menu_title='Analisis',
                options=['Contexto Historico','EDA Consumo','EDA Adictos','Predicción de consumo','Predicción de Adicciones'],
                icons=['signpost-split','bar-chart-fill','reception-3','capsule','capsule'],
                menu_icon=':cyclone:',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'#212F3D '},
        "icon": {"color": "white", "font-size": "20px"}, 
        "nav-link": {"color":"white","font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#F7DC6F"},
        "nav-link-selected": {"background-color": "#FFA07A"},}
                
                )

        
        if app == "Contexto Historico":
            contexto_Historico.app()
        if app == "EDA Consumo":
            EDA_Consumo.app()    
        if app == "EDA Adictos":
            EDA_Adictos.app()        
        if app == 'Predicción de consumo':
            Simulaciones_pag4.app()
        if app == 'Predicción de Adicciones':
            Predicción.app()    
             
          
             
    run()    