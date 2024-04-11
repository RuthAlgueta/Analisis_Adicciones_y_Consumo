# ---- Librerías ----
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
from matplotlib import pyplot as plt
import numpy as np
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
from io import StringIO
import base64




# ---- Configuración de la página ----
# st.set_page_config(page_title="USO DE DROGAS Y FACTORES DE RIESGO ASOCIADOS", layout="centered", page_icon="💊")

def app():
    
    titulo_html = """
    <h1 style='text-align: center; color: #FFA07A; font-size: 35px;'>
        Consumo de Sustancias de 1971-2018 en Estados Unidos💊
    </h1>
""" 
    st.write(" ")
    st.markdown(titulo_html, unsafe_allow_html=True)
    st.write(" ")
    st.write(" ")
   
    # ---- Carga del archivo y preprocesamiento ----
    df = pd.read_csv("data/drugs_and_riskfactors.csv")
    col1, col2, = st.columns(2)
    with col1:
        st.header("Objetivo del proyecto")

        st.markdown("""Este proyecto tiene como objetivo explorar cómo ciertos factores de riesgo afectan el consumo de drogas. Mediante este estudio, se busca analizar el impacto de diversas variables en la probabilidad de convertirse en consumidor junto con variables socioeconómicas y demográficas (edad, educación, ingresos, raza, genero, empleo). Se utilizarán datos específicos para identificar estos factores y su correlación con el uso de sustancias. Finalmente, se estimarán las probabilidades de consumo según las variables analizadas.
                          """)
        st.markdown(""" Que es una adicion? Es una enfermedad crónica y recurrente del cerebro que se caracteriza por una búsquerda constante de la recompensa y/o alivio a través del uso de una sustancia u otras conductas.
                          """)
        
        st.markdown("""web de datos : https://www.datafiles.samhsa.gov/data-sources
                    Este conjunto de datos fue extraído de la Encuesta Nacional de 2018 sobre el Uso de Drogas y la Salud, que es una encuesta anual (a partir de 1971) que recopila datos sobre el uso de drogas y problemas de salud mental en los Estados Unidos. La encuesta es realizada por la Administración de Servicios de Abuso de Sustancias y Salud Mental (SAMHSA) https://nsduhweb.rti.org/respweb/homepage.cfm. https://www.datafiles.samhsa.gov/dataset/national-survey-drug-use-and-health-2020-nsduh-2020-ds0001.
                    Contiene 16 características categóricas de 56,136 observaciones. """)

    with col2:
        #st.image("img/adicciones-01.png")
        #st.image("img/icono_drogas.jpg")
    #with col3:
        st.image("img/tablon.png",width=305)
        #st.image("img/icono_drogas.jpg")
       

    # Código para codificar la imagen en base64
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
         data = f.read()
        return base64.b64encode(data).decode()

    encoded_image = get_base64_of_bin_file("img/marihuana-01.png")

    # Mostrar la imagen con transparencia
    st.markdown(
        f"""
        <div style="opacity: 0.5;">
            <img src="data:image/png;base64,{encoded_image}" style="width:100%">
        </div>
        """,
        unsafe_allow_html=True
    )

    






# Ejecuta la app
if __name__ == "__main__":
    app()