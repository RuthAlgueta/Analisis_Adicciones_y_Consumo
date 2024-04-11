#librerias
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import pandas as pd
import base64



def app():
    # Carga del df
    df = pd.read_csv('C:/Users/rutha/Desktop/SAMPLEREPO/03_Modulo_3/7_proyecto_Final/data/dfPrediccion.csv')


    container = st.container()
    with container:
            st.markdown(
                    """
                            <div style='background-color: #FFA07A; border-radius: 10px; padding: 20px; text-align: center; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3); margin-top: 10px; margin-left: auto; margin-right: auto; width: fit-content;'>
                            <div style='font-size: 30px; font-weight: 700; margin-bottom: 15px; color: #ffffff;'>Predicción de de la media de personas por estado, adictas al Alcohol , Tabaco y Marihuana.</div>
                            </div>
                            """,
                                    unsafe_allow_html=True
            )
            


            titulo_html = """
                    <h1 style='text-align: center; color: white; font-size: 15px;'>
                             
                    </h1>
                    """
            st.markdown(titulo_html, unsafe_allow_html=True)




    # Mostrar columna 
    
    col1, col2, col3 = st.columns(3)
    with col2:
        # Agregar estilo CSS a la columna col2.
        col2.markdown(
            f"""
            <style>
                .css-1pahdxg {{
                    background-color: #2AB09C;
                    color: white;
                }}
            </style>
            """,
            unsafe_allow_html=True
        )



    titulo_html = """
                    <h1 style='text-align: center; color: white; font-size: 20px;'>
                            Promedio del Consumo  de sustancias  en 2018 por estados . 
                    </h1>
                    """
    
    st.markdown(titulo_html, unsafe_allow_html=True)
   
   
   #---------------------grafico del 2018--------------------



    # Filtrar datos para el año 2018
    df_2018 = df[df['Año'] == 2018]

    # Suma de las variables
    total_alcoholicos = df_2018['total_de_Alcoholicos+26'].sum().astype(int)
    total_fumadores = df_2018['total_fumadores'].sum().astype(int)
    total_marihuana = df_2018['consumen_Marihuana'].sum().astype(int)
    
    num_estados = 51
    media_alcoholicos = int(total_alcoholicos / num_estados)
    media_adictos_tabaco = int(total_fumadores / num_estados)
    media_adictos_marihuana = int(total_marihuana / num_estados)


    # Crear gráfico de barras
    fig = go.Figure()
    
    fig.add_trace(go.Bar(x=['Adictos Tabaco'], y=[media_adictos_tabaco], name='Adictos Tabaco', marker_color='orange'))
    fig.add_trace(go.Bar(x=['Adictos Marihuana'], y=[media_adictos_marihuana], name='Adictos Marihuana', marker_color='green'))
    fig.add_trace(go.Bar(x=['Alcohólicos'], y=[media_alcoholicos], name='Alcohólicos', marker_color='skyblue'))
    fig.update_layout(title_text='Promedio de Consumidores por Sustancia en 2018', title_x=0.5, xaxis_title='Sustancias', yaxis_title='Promedio (personas)', legend_title='Categoría')

    # Mostrar gráfico en Streamlit
    st.plotly_chart(fig)

   

    st.write('')
    st.write('')



#--------Seleccione el año para obtener la media de personas por Estado, que seran adictas.

    container = st.container()
    with container:
            st.markdown(
                    """
                            <div style='background-color: #363A43; border-radius: 10px; padding: 10px; text-align: center; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3); margin-top: 10px; margin-left: auto; margin-right: auto; width: fit-content;'>
                            <div style='font-size: 30px; font-weight: 700; margin-bottom: 2px; color: #ffffff;'>Haga click en el botón 'Predecir'.</div>
                            </div>
                            """,
                                    unsafe_allow_html=True
            )
            


            titulo_html = """
                    <h1 style='text-align: center; color: white; font-size: 15px;'>
                            Seleccione el año para obtener la media de personas por Estado, que seran adictas
                    </h1>
                    """
            st.markdown(titulo_html, unsafe_allow_html=True)

    st.write('')
    st.write('')


    #----------------LinearRegression--------------------------------------------------
   


  # Divide los datos
    X = df[['Año']]
    y = df[['total_fumadores', 'consumen_Marihuana', 'total_de_Alcoholicos+26']]

    # Realiza la división de los datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Inicializa y entrena el modelo
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Nombres correspondientes a las variables de predicción y unidades de medida
    variables = ['Total Adictos al tabaco', 'Total Adictos a la Marihuana', 'Total de Alcohólicos']
    units = ['personas', 'personas', 'personas']

    # La interfaz de la aplicación en Streamlit
    st.markdown("""<h3 style='text-align: center; color: grey;'></h3>""", unsafe_allow_html=True)

    year_to_predict = st.select_slider('Seleccione el año para predecir', options=list(range(2025, 2033)), value=2025)

    if st.button('Predecir'):
        # Realiza la predicción para el año seleccionado
        y_pred = model.predict([[year_to_predict]])
        y_pred = y_pred.flatten()

        # Presentar los resultados con valores enteros y unidades de medida
        prediction_text = f"""<div>
                <p>La predicción para el año <strong>{year_to_predict}</strong> es:</p>
                <ul>
                    <li>{variables[0]}: <strong>{int(y_pred[0])}</strong> {units[0]}</li>
                    <li>{variables[1]}: <strong>{int(y_pred[1])}</strong> {units[1]}</li>
                    <li>{variables[2]}: <strong>{int(y_pred[2])}</strong> {units[2]}</li>
                </ul>
            </div>"""
        
        st.markdown(prediction_text, unsafe_allow_html=True)
        
        # Visualización de la predicción para varios años con gráfico de barras
        years = list(range(2025, 2033))
        predictions = [model.predict([[year]]) for year in years]
        predictions_flattened = [pred.flatten() for pred in predictions]
        
        # Gráfico de barras para el año seleccionado
        fig_single_year = go.Figure()
        
        fig_single_year.add_trace(go.Bar(
            x=[f"{variables[0]}<br>({int(y_pred[0])} {units[0]})", 
            f"{variables[1]}<br>({int(y_pred[1])} {units[1]})", 
            f"{variables[2]}<br>({int(y_pred[2])} {units[2]})"],
            
            y=[int(val) for val in y_pred],
            marker_color=['orange', 'green', 'skyblue']
        ))

        fig_single_year.update_layout(
            title_text=f'Predicción del Consumo de Sustancias para el Año {year_to_predict}',
            title_x=0.5,
            xaxis_title='Sustancia',
            yaxis_title='Cantidad de Consumidores',
            bargap=0.4  # Espacio entre las barras
        )
        
        # Mostrar los gráficos
        st.plotly_chart(fig_single_year)




#-------------------imagen final 
        
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

    

#--------------------------------------GRAFICO DE EDAD BIGOTES





# Ejecuta la app
if __name__ == "__main__":
    app()
