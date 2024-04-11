# ---- Librerías ----
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
from matplotlib import pyplot as plt
import numpy as np
import base64

from streamlit_option_menu import option_menu


# ---- Configuración de la página ----
# st.set_page_config(page_title="USO DE DROGAS Y FACTORES DE RIESGO ASOCIADOS", layout="centered", page_icon="💊")

def app():
    #st.title('Consumo de Drogas de 1992 - 2019 en Estados Unidos💊')
  
    # ---- Carga del archivo y preprocesamiento ----
    df = pd.read_csv("data/drugs_and_riskfactors.csv")
    

    def main():
        

        titulo_html = """
        <h1 style='text-align: center; color: #FFA07A; font-size: 35px;'>
            Consumo de Drogas recreativas mas prevalentes en La sociedad Americana de 1971 - 2018💊
        </h1>
    """ 
        st.write('')
        st.write('')

        st.markdown(titulo_html, unsafe_allow_html=True)


        titulo_html = """
        <h1 style='text-align: center; color: white; font-size: 25px;'>
            Análisis Exploratorio de Datos
        </h1>
    """ 
        st.write('')
     

        st.markdown(titulo_html, unsafe_allow_html=True)
        
        
        
        
        #st.title("Análisis Exploratorio de Datos")
        # Renombrando columnas para claridad
        df_c = df[['age', 'education', 'father', 'mother', 'income', 'race', 'sex', 'employment']].rename(
            columns={'age': 'edad', 'education': 'Educación', 'father': 'Convivencia_Padre', 
                     'mother': 'Convivencia_Madre', 'income': 'Ingresos', 'race': 'Raza', 
                     'sex': 'Género', 'employment': 'Empleo'})

        df_d = df[['alcohol', 'cigarettes', 'cocaine', 'crack', 'heroin', 'marijuana', 'meth', 'pain_relievers']].rename(
            columns={'alcohol': 'Alcohol', 'cigarettes': 'Tabaco', 'cocaine': 'Cocaina', 
                     'crack': 'Crack', 'heroin': 'Heroina', 'marijuana': 'Marihuana', 
                     'meth': 'Metanfetamina', 'pain_relievers': 'Analgésicos'})

        df_2 = df_c.join(df_d)


        st.write(" ")
        st.write(" ")
#--------------------------------------------------GRAFICOS DE VARIABLES CATEGORICAS  ---------------------------

        # Mapeos definidos para las categorías
        mapeos = {
            'edad': {
                1: 'De 12 a 17 años',
                2: 'De 18 a 25 años',
                3: 'De 26 a 34 años',
                4: 'De 35 a 49 años',
                5: 'De 50 a 64 años',
                6: '65 años o más'
            },
            'Educación': {
                1: 'No graduado de la secundaria',
                2: 'Graduado de la secundaria',
                3: 'Algo de universidad, o título de asociado',
                4: 'Graduado universitario',
                5: 'De 12 a 17 años'
            },
            'Empleo': {
                1: 'El participante está empleado a tiempo completo',
                2: 'El participante está empleado a tiempo parcial',
                3: 'El participante está desempleado',
                4: 'Otro (incl. no en la fuerza laboral)',
                99: 'El participante es menor de edad; de 12 a 14 años'
            },
            'Convivencia_Padre': {
                1: 'Sí, el padre está en el hogar',
                2: 'No, el padre no está en el hogar',
                3: 'No se sabe',
                4: 'el participante tiene 18 años o más'
            },
            'Ingresos': {
                1: 'Menos de $20,000',
                2: 'Entre $20,000 y $49,000',
                3: 'Entre $50,000 y $74,999',
                4: 'Más de $75,000'
            },
            'Convivencia_Madre': {
                1: 'Sí, la madre está en el hogar',
                2: 'No, la madre no está en el hogar',
                3: 'No sabe se sabe',
                4: 'el participante tiene 18 años o más'
            },
            'Raza': {
                1: 'Blanco',
                2: 'Negro',
                3: 'Nativo Americano',
                4: 'Nativo Hawaiano/Islas del Pacífico',
                5: 'Asiático',
                6: 'Multirracial',
                7: 'Hispano'
            },
            'Género': {
                1: 'El participante es masculino',
                2: 'El participante es femenino'
            }
        }

        # Configuración del título y selección de la variable categórica
        st.header("Visualización de Variables Categóricas")
        option = st.selectbox(
            '¿Qué variable categórica te gustaría visualizar?',
            ['edad', 'Educación', 'Raza', 'Género', 'Empleo','Ingresos','Convivencia_Madre','Convivencia_Padre']
        )

        # Adaptación a Plotly con mapeos
        if option in mapeos:
            # Aplicando el mapeo al DataFrame
            df_2[option] = df_2[option].map(mapeos[option])
            # Creando visualización
            counts = df_2[option].value_counts().reset_index()
            counts.columns = ['Variables de Factores de Riesgo', 'count']
            fig = px.bar(counts, x='Variables de Factores de Riesgo', y='count', title=f'Distribución de {option}')
        else:
            # Para otras opciones, contamos los valores y usamos un gráfico de barras (este bloque podría ser innecesario dado el mapeo proporcionado)
            counts = df_2[option].value_counts().reset_index()
            counts.columns = [option, 'count']
            fig = px.bar(counts, x=option, y='count', title=f'Distribución de {option}')

        st.plotly_chart(fig)


        st.write(" ")
        st.write(" ")
#-------------------------------------------------------------GRAFICO 02---------------------------------------------------

        # Visualización de sustancias usando Plotly y colores personalizados
        st.header('Visualización de Consumo de Sustancias')
        selected_columns = st.multiselect(
            'Selecciona las sustancias que deseas analizar',
            options=["Alcohol", "Tabaco", "Cocaina", "Crack", "Heroina", "Marihuana", "Metanfetamina", "Analgésicos"],
            default=["Alcohol", "Tabaco", "Marihuana"]
        )

        if selected_columns:
            # Filtrando datos seleccionados
            substance_data = df_2[selected_columns]

            # Calculando totales
            substance_totals = substance_data.sum().reset_index()
            substance_totals.columns = ['Substance', 'Total']

            # Mapa de colores predefinido
            color_map = {
                "Alcohol": "skyblue", "Tabaco": "orange", "Marihuana": "green",
                "Crack": "red", "Heroina": "purple", "Cocaina": "brown",
                "Metanfetamina": "pink", "Analgésicos": "grey"
            }

            # Filtrando mapa de colores para coincidir con la selección del usuario
            filtered_color_map = {key: color_map[key] for key in selected_columns if key in color_map}

            # Creando y mostrando el gráfico final
            fig = px.bar(substance_totals, x='Substance', y='Total', text_auto=True,
                        title="Total de Reportes por Sustancia",
                        labels={"Substance": "Tipo de Sustancia", "Total": "Total de Reportes"},
                        color='Substance', color_discrete_map=filtered_color_map)
            st.plotly_chart(fig)
        else:
            st.warning('Selecciona al menos una sustancia.')
            st.stop()



        st.write(" ")
        st.write(" ")
#-----------------------------------------------graficos de CORRELACION 03  --------------------------------

        titulo_html = """
                <h1 style='text-align: center; color: #FFA07A; font-size: 35px;'>
                    Graficos de correlación💊
                </h1>
            """ 
                
        st.markdown(titulo_html, unsafe_allow_html=True)





        #-----------------------------------------------matriz de correlacion
        


        # Crear matriz de correlación
        corr = df_d.corr()

        # Configurar la figura
        plt.figure(figsize=(12, 10))

        # Crear heatmap con fondo transparente
        sns.heatmap(corr, annot=True, cmap='coolwarm', alpha=0.7)

        # Añadir título al gráfico
        plt.title("Mapa de Calor de Correlación")

        # Mostrar el gráfico en Streamlit
        st.pyplot()
        st.set_option('deprecation.showPyplotGlobalUse', False)

        st.write('')
        st.write('')
        st.write('')
       
        st.write('')
        st.write('')


#------------------------boton ----------------------

        # Agregar un selectbox para elegir el gráfico a visualizar
        selected_chart = st.selectbox("Selecciona un gráfico para visualizar", ["Consumo de Tabaco, Alcohol y Ambos por Educación",
                                                                            "Consumo de Tabaco, Alcohol y Ambos por Edad",
                                                                            "Consumo de Tabaco, Alcohol, Marihuana y Ambos por Edad",
                                                                            "Consumo de Tabaco, Marihuana y Ambos por Edad",
                                                                            "Consumo de Analgésicos, Marihuana y Ambos por Edad",
                                                                            "Consumo de Analgésicos, Marihuana y Ambos por Raza",
                                                                            "Consumo de Tabaco, Alcohol y Ambos por Género",])

       











#------------------------------'edad', 'Educación', 'Raza', 'Género', 'Empleo']------------------------inicio grafico Educaacion

        # GRAFICO: Consumo de Tabaco, Alcohol y Ambos por Educación

        # Crear una nueva columna que indique si consumen ambas sustancias 'Tabaco' y 'Alcohol'
        df_2['consume_both'] = df_2['Tabaco'] & df_2['Alcohol']

        # Contar el número de personas que consumen 'Tabaco', 'Alcohol' y ambos por Educación
        consumption_by_education = df_2.groupby('Educación')[['Tabaco', 'Alcohol', 'consume_both']].mean().reset_index()

        # Mapeo de Educación a categorías
        mapeos = {
                1: 'No graduado de la secundaria',
                2: 'Graduado de la secundaria',
                3: 'Algo de universidad, o título de asociado',
                4: 'Graduado universitario',
                5: 'De 12 a 17 años'
        }

        # Mapear los valores de 'Educación' a las categorías descriptivas
        consumption_by_education['Educación'] = consumption_by_education['Educación'].map(mapeos)

        # Crear el gráfico interactivo de barras utilizando Plotly Express
        fig1 = px.bar(consumption_by_education, x='Educación', y=['Tabaco', 'Alcohol', 'consume_both'],
                    title='Consumo de Tabaco, Alcohol y Ambos por Educación',
                    labels={'value': 'Cantidad de Consumidores', 'variable': 'Sustancia', 'Educación': 'Educación'},
                    barmode='group',  # Agrupar las barras para cada educación
                    color_discrete_map={'Tabaco': 'orange', 'Alcohol': 'skyblue', 'consume_both': '#EFFF8B'})  # Definir colores para las barras

        # Personalizar el diseño del gráfico
        fig1.update_layout(
            xaxis_title='Educación',
            yaxis_title='Cantidad de Consumidores',
            legend_title='Sustancia',
            legend=dict(
                yanchor="top",
                y=1.2,
                xanchor="left",
                x=0.9 
            )
        )

        # Mostrar el gráfico en Streamlit sin el fondo
        #st.plotly_chart(fig1, use_container_width=True)

        st.write(" ")
        st.write(" ")


#-------------------------------------------------------------------------------------------------------------inicio grafico Edad
        #GRAFICO : Consumo de Tabaco, Alcohol y Ambos por Edad

        # Crear una nueva columna que indique si consumen ambas sustancias 'Tabaco' y 'Alcohol'
        df_2['consume_both'] = (df_2['Tabaco'] & df_2['Alcohol'])

        # Contar el número de personas que consumen 'Tabaco', 'Alcohol' y ambos por edad
        consumption_by_age = df_2.groupby('edad')[['Tabaco', 'Alcohol', 'consume_both']].mean().reset_index()

        # Mapeo de edad a categorías
   
        # Asignando las etiquetas de edad a los valores de 'age'
        consumption_by_age['edad'] = consumption_by_age['edad']

        # Crear el gráfico interactivo de barras utilizando Plotly Express
        fig2 = px.bar(consumption_by_age, x='edad', y=['Tabaco', 'Alcohol', 'consume_both'],
                        title='Consumo de Tabaco, Alcohol y Ambos por Edad',
                        labels={'value':'Cantidad de Consumidores', 'variable':'Sustancia', 'edad':'Edad'},
                        barmode='group',  # Agrupar las barras para cada edad
                        color_discrete_map={'Tabaco': 'orange', 'Alcohol': 'skyblue', 'consume_both': '#EFFF8B'})  # Definir colores para las barras

        # Personalizar el diseño del gráfico
        fig2.update_layout(
            xaxis_title='Edad',
            yaxis_title='Cantidad de Consumidores',
            legend_title='Sustancia',
            legend=dict(
                yanchor="top",
                y=1.1,
                xanchor="left",
                x=0.9
            )
        )


        #st.plotly_chart(fig2, use_container_width=True)

#------------------------------------------------Grafico marihuana ------------------------------------------

        #GRAFICO: Consumo de Tabaco, Alcohol, Marihuana y Ambos por Edad

 # Crear una nueva columna que indique si consumen ambas sustancias 'Tabaco' y 'Alcohol''Marihuana'
        df_2['consume_both'] = (df_2['Tabaco'] & df_2['Alcohol']& df_2['Marihuana'])

        # Contar el número de personas que consumen 'Tabaco', 'Alcohol' y ambos por edad
        consumption_by_age = df_2.groupby('edad')[['Tabaco', 'Alcohol','Marihuana', 'consume_both']].mean().reset_index()

        # Mapeo de edad a categorías
   
        # Asignando las etiquetas de edad a los valores de 'age'
        consumption_by_age['edad'] = consumption_by_age['edad']

        # Crear el gráfico interactivo de barras utilizando Plotly Express
        fig3 = px.bar(consumption_by_age, x='edad', y=['Tabaco', 'Alcohol', 'Marihuana', 'consume_both'],
                        title='Consumo de Tabaco, Alcohol, Marihuana y Ambos por Edad',
                        labels={'value':'Cantidad de Consumidores', 'variable':'Sustancia', 'edad':'Edad'},
                        barmode='group',  # Agrupar las barras para cada edad
                        color_discrete_map={'Tabaco': 'orange', 'Alcohol': 'skyblue', 'Marihuana': 'green','consume_both': '#EFFF8B'})  # Definir colores para las barras

        # Personalizar el diseño del gráfico
        fig3.update_layout(
            xaxis_title='Edad',
            yaxis_title='Cantidad de Consumidores',
            legend_title='Sustancia',
            legend=dict(
                yanchor="top",
                y=1.1,
                xanchor="left",
                x=0.9
            )
        )

        #st.plotly_chart(fig3, use_container_width=True)



#---------------------------------------------GRAFICO MARIHUANA Y TABACO
            
            #GRAFICO: Consumo de Tabaco, Marihuana y Ambos por Edad

 # Crear una nueva columna que indique si consumen ambas sustancias 'Tabaco' 'Marihuana'
        df_2['consume_both'] = (df_2['Tabaco'] & df_2['Marihuana'])

        # Contar el número de personas que consumen 'Tabaco', Y MARIHUANA y ambos por edad
        consumption_by_age = df_2.groupby('edad')[['Tabaco', 'Marihuana', 'consume_both']].mean().reset_index()

        # Mapeo de edad a categorías
   
        # Asignando las etiquetas de edad a los valores de 'age'
        consumption_by_age['edad'] = consumption_by_age['edad']

        # Crear el gráfico interactivo de barras utilizando Plotly Express
        fig4 = px.bar(consumption_by_age, x='edad', y=['Tabaco', 'Marihuana', 'consume_both'],
                        title='Consumo de Tabaco, Marihuana y Ambos por Edad',
                        labels={'value':'Cantidad de Consumidores', 'variable':'Sustancia', 'edad':'Edad'},
                        barmode='group',  # Agrupar las barras para cada edad
                        color_discrete_map={'Tabaco': 'orange', 'Marihuana': 'green','consume_both': '#EFFF8B'})  # Definir colores para las barras

        # Personalizar el diseño del gráfico
        fig4.update_layout(
            xaxis_title='Edad',
            yaxis_title='Cantidad de Consumidores',
            legend_title='Sustancia',
            legend=dict(
                yanchor="top",
                y=1.1,
                xanchor="left",
                x=0.9
            )
        )

        #st.plotly_chart(fig4, use_container_width=True)





#---------------------------------------------GRAFICO MARIHUANA Y "Analgésicos": "grey


            #GRAFICO:Consumo de Analgésicos, Marihuana y Ambos por Edad

 # Crear una nueva columna que indique si consumen ambas sustancias 'Tabaco' 'Marihuana'
        df_2['consume_both'] = (df_2['Analgésicos'] & df_2['Marihuana'])

        # Contar el número de personas que consumen 'Tabaco', Y MARIHUANA y ambos por edad
        consumption_by_age = df_2.groupby('edad')[['Analgésicos', 'Marihuana', 'consume_both']].mean().reset_index()

        # Mapeo de edad a categorías
   
        # Asignando las etiquetas de edad a los valores de 'age'
        consumption_by_age['edad'] = consumption_by_age['edad']

        # Crear el gráfico interactivo de barras utilizando Plotly Express
        fig5 = px.bar(consumption_by_age, x='edad', y=['Analgésicos', 'Marihuana', 'consume_both'],
                        title='Consumo de Analgésicos, Marihuana y Ambos por Edad',
                        labels={'value':'Cantidad de Consumidores', 'variable':'Sustancia', 'edad':'Edad'},
                        barmode='group',  # Agrupar las barras para cada edad
                        color_discrete_map={'Analgésicos': 'grey', 'Marihuana': 'green','consume_both': '#EFFF8B'})  # Definir colores para las barras

        # Personalizar el diseño del gráfico
        fig5.update_layout(
            xaxis_title='Edad',
            yaxis_title='Cantidad de Consumidores',
            legend_title='Sustancia',
            legend=dict(
                yanchor="top",
                y=1.1,
                xanchor="left",
                x=0.9
            )
        )

        # Mostrar el gráfico en Streamlit sin el fondo
        #st.plotly_chart(fig5, use_container_width=True)

#--------------------------------------GRAFICO RAZA

#GRAFICO:Consumo de Analgésicos, Marihuana y Ambos por Raza

 # Crear una nueva columna que indique si consumen ambas sustancias 'Tabaco' 'Marihuana'
        df_2['consume_both'] = (df_2['Analgésicos'] & df_2['Marihuana'])

        # Contar el número de personas que consumen 'Tabaco', Y MARIHUANA y ambos por Raza
        consumption_by_Raza = df_2.groupby('Raza')[['Analgésicos', 'Marihuana', 'consume_both']].mean().reset_index()

        # Mapeo de Raza a categorías
   # Mapeo de Educación a categorías
        mapeos = {
                1: 'Blanco',
                2: 'Negro',
                3: 'Nativo Americano',
                4: 'Nativo Hawaiano/Islas del Pacífico',
                5: 'Asiático',
                6: 'Multirracial',
                7: 'Hispano'
        } 

        # Mapear los valores de 'Educación' a las categorías descriptivas
        consumption_by_Raza['Raza'] = consumption_by_Raza['Raza'].map(mapeos)
   

     


        # Crear el gráfico interactivo de barras utilizando Plotly Express
        fig6 = px.bar(consumption_by_Raza, x='Raza', y=['Analgésicos', 'Marihuana', 'consume_both'],
                        title='Consumo de Analgésicos, Marihuana y Ambos por Raza',
                        labels={'value':'Cantidad de Consumidores', 'variable':'Sustancia', 'Raza':'Raza'},
                        barmode='group',  # Agrupar las barras para cada Raza
                        color_discrete_map={'Analgésicos': 'grey', 'Marihuana': 'green','consume_both': '#EFFF8B'})  # Definir colores para las barras

        # Personalizar el diseño del gráfico
        fig6.update_layout(
            xaxis_title='Raza',
            yaxis_title='Cantidad de Consumidores',
            legend_title='Sustancia',
            legend=dict(
                yanchor="top",
                y=1.1,
                xanchor="left",
                x=0.9
            )
        )

        #st.plotly_chart(fig6, use_container_width=True)

#---------------------------------------------------------------------------inicio grafico Edad


        #GRAFICO : Consumo de Tabaco, Alcohol y Ambos por Edad

        # Crear una nueva columna que indique si consumen ambas sustancias 'Tabaco' y 'Alcohol'
        df_2['consume_both'] = (df_2['Tabaco'] & df_2['Alcohol'])

        # Contar el número de personas que consumen 'Tabaco', 'Alcohol' y ambos por edad raza
        consumption_Género = df_2.groupby('Género')[['Tabaco', 'Alcohol', 'consume_both']].mean().reset_index()

        # Mapeo de edad a categorías
        mapeos = {
                        1: 'El participante es masculino',
                        2: 'El participante es femenino',} 

        #consumption_Género Mapear los valores de 'Educación' a las categorías descriptivas
        consumption_Género['Género'] = consumption_Género['Género'].map(mapeos)
        # Asignando las etiquetas de edad a los valores de 'age'
        #consumption_by_age['Género'] = consumption_by_age['edad']

        # Crear el gráfico interactivo de barras utilizando Plotly Express
        fig7 = px.bar(consumption_Género, x='Género', y=['Tabaco', 'Alcohol', 'consume_both'],
                        title='Consumo de Tabaco, Alcohol y Ambos por Edad',
                        labels={'value':'Cantidad de Consumidores', 'variable':'Sustancia', 'Género':'Género'},
                        barmode='group',  # Agrupar las barras para cada edad
                        color_discrete_map={'Tabaco': 'orange', 'Alcohol': 'skyblue', 'consume_both': '#EFFF8B'})  # Definir colores para las barras

        # Personalizar el diseño del gráfico
        fig7.update_layout(
            xaxis_title='Género',
            yaxis_title='Cantidad de Consumidores',
            legend_title='Sustancia',
            legend=dict(
                yanchor="top",
                y=1.1,
                xanchor="left",
                x=0.9
            )
        )

       

# ----------------------------------final BOTON
 # Mostrar el gráfico seleccionados por el boton  
        if selected_chart == "Consumo de Tabaco, Alcohol y Ambos por Educación":
            st.plotly_chart(fig1, use_container_width=True)
        elif selected_chart == "Consumo de Tabaco, Alcohol y Ambos por Edad":
            st.plotly_chart(fig2, use_container_width=True)
        elif selected_chart == "Consumo de Tabaco, Alcohol, Marihuana y Ambos por Edad":
            st.plotly_chart(fig3, use_container_width=True)
        elif selected_chart == "Consumo de Tabaco, Marihuana y Ambos por Edad":
            st.plotly_chart(fig4, use_container_width=True)
        elif selected_chart == "Consumo de Analgésicos, Marihuana y Ambos por Edad":
            st.plotly_chart(fig5, use_container_width=True)
        elif selected_chart == "Consumo de Analgésicos, Marihuana y Ambos por Raza":
            st.plotly_chart(fig6, use_container_width=True)
        elif selected_chart == "Consumo de Tabaco, Alcohol y Ambos por Género":
            st.plotly_chart(fig7, use_container_width=True)


        st.write('')


            # Código para codificar la imagen en base64
        def get_base64_of_bin_file(bin_file):
            with open(bin_file, 'rb') as f:
                data = f.read()
            return base64.b64encode(data).decode()

        encoded_image = get_base64_of_bin_file("img/adicciones-01.png")

            # Mostrar la imagen con transparencia
        st.markdown(
                f"""
                <div style="opacity: 0.3;">
                    <img src="data:image/png;base64,{encoded_image}" style="width:100%">
                </div>
                """,
                unsafe_allow_html=True
            )


    main()


# Ejecuta la app
if __name__ == "__main__":

    app()


