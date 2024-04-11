# ---- Librerías de Visualización ----
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from io import BytesIO
from sklearn.linear_model import LinearRegression
from io import BytesIO
import streamlit.components.v1 as components
import base64
from streamlit_option_menu import option_menu

# Crear un DataFrame con los datos proporcionados
df_nuevo = pd.read_csv('C:/Users/rutha/Desktop/SAMPLEREPO/03_Modulo_3/7_proyecto_Final/data/Adictos_Analisis.csv')
Droga = pd.read_csv('C:/Users/rutha/Desktop/SAMPLEREPO/03_Modulo_3/7_proyecto_Final/data/Df_tendencia.csv')
df_nuevo2 = pd.read_csv('C:/Users/rutha/Desktop/SAMPLEREPO/03_Modulo_3/7_proyecto_Final/data/AdictosHabitantes.csv')

# Interfaz de la App Streamlit
def app():
    titulo_html = """
                <h1 style='text-align: center; color: #FFA07A; font-size: 35px;'>
                    Adictos en la sociedad Americana con diagnóstico del Departamento de Salud (HHS) de 2002 a 2018
                </h1>
            """
    st.write('')
    st.markdown(titulo_html, unsafe_allow_html=True)

    titulo_html = """
        <h1 style='text-align: center; color: white; font-size: 25px;'>
            Análisis Exploratorio de Datos
        </h1>
    """

    st.markdown(titulo_html, unsafe_allow_html=True)

    st.write('')
    st.write('')

    # --------------------- Gráfico 1 - Media de alcholicos por estado ---------------------
    st.write('')
  

#####----------------------------------explorar datos :
  
    titulo_html = """
                <h1 style='text-align: center; color: #FFA07A; font-size: 23px;'>
                    En este dataset hay 197 millones de habitantes obtenidos haciendo un promedio de los 17 años, no es el total de todos los habitantes de USA, ya que son un total de 331 millones 
                </h1>
            """
    st.markdown(titulo_html, unsafe_allow_html=True) 

#####--------

# Calcular la media de Alcoholicos, Adictos_tabaco, Adictos_Marihuana y Habitantes por estado
  

    suma_alcoholicos = df_nuevo2['Alcoholicos'].sum()
    suma_adictos_tabaco= df_nuevo2['Adictos_tabaco'].sum()
    suma_adictos_marihuana= df_nuevo2['Adictos_Marihuana'].sum()
    suma_habitantes= df_nuevo2['Habitantes'].sum()/17

    num_estados = 51
    media_alcoholicos = int(suma_alcoholicos / num_estados)
    media_adictos_tabaco = int(suma_adictos_tabaco / num_estados)
    media_adictos_marihuana = int(suma_adictos_marihuana / num_estados)
    media_habitantes = int(suma_habitantes / num_estados)
    
    # Muestra los resultados en Streamlit
    #st.header("SumayMedia de Adicciones por Estado")

    #Agrega un punto cada 3 números empezando por la derecha a los resultados
    media_alcoholicos = "{:,}".format(media_alcoholicos)
    media_adictos_tabaco = "{:,}".format(media_adictos_tabaco)
    media_adictos_marihuana= "{:,}".format(media_adictos_marihuana)
    media_habitantes= "{:,}".format(media_habitantes)

#------------------version columnas



    variables = {
        'Alcohólicos': media_alcoholicos,
        'Adictos al tabaco': media_adictos_tabaco,
        'Adictos a Marihuana': media_adictos_marihuana,
        'Habitantes': media_habitantes
    }

    cols = st.columns(4)  # Crear 4 columnas

    for i, (variable, media) in enumerate(variables.items()):
        with cols[i % 4]:  # Distribuir cada variable en una de las columnas
            st.markdown(
                f"""
                <h2 style='font-size: 15px; text-align: center; color: white;'>
                    Media de {variable} por estados
                </h2>
                <div style='background-color: #FFA07A; border-radius: 12px; padding: 10px; text-align: center; 
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3); margin-top: 10px; margin-left: auto; margin-right: auto;
                width: fit-content;'>
                    <div style='font-size: 20px; font-weight: 700; margin-bottom: 2px; color: #ffffff;'>
                        {media} personas <i class="bar-chart-fill"style="font-size: 20px; color: #FFFFFF;"></i>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )



    st.write('')
    st.write('')
    st.write('')


#-------------------------------grafico 

     
    # --------------------- Gráfico 002 - cantidad de habitantes por estado mayores de 26 ---------------------
    st.write('')
    st.write('')

    summary = df_nuevo2.drop(columns=['Año']).mean().reset_index()
    summary.columns = ['Sustancia', 'Numero de personas']

 

    media_por_estado = df_nuevo2.groupby('Estado')['Habitantes'].mean().reset_index()
    media_por_estado['Habitantes'] = media_por_estado['Habitantes'].astype(int)

    fig = px.bar(media_por_estado, x='Estado', y='Habitantes', color='Estado',
                labels={'Habitantes': 'Numero de Habitantes'},
                title='Cantidad de Habitantes por Estado mayores de 26 años', template='plotly_dark')

    st.plotly_chart(fig)
   
   
   #----------------------------grafico todos 
   


    # Media de Alcohólicos por Estado mayores de 26 años
    media_alcoholicos = df_nuevo2.groupby('Estado')['Alcoholicos'].mean().reset_index()
    media_alcoholicos['Alcoholicos'] = media_alcoholicos['Alcoholicos'].astype(int)

    # Media de Habitantes por Estado mayores de 26 años
    media_habitantes = df_nuevo2.groupby('Estado')['Habitantes'].mean().reset_index()
    media_habitantes['Habitantes'] = media_habitantes['Habitantes'].astype(int)

    # Calcular la media de Alcohólicos por estado
    media_alcoholicos_estados = media_alcoholicos['Alcoholicos'].mean()

    # Combina la información de Alcoholicos y Habitantes por Estado en un solo DataFrame
    combined_data = pd.merge(media_alcoholicos, media_habitantes, on='Estado', how='inner')

    # Crea el gráfico combinado de Alcohólicos vs Habitantes por Estado con la línea de media de Alcohólicos por estado
    fig = px.bar(combined_data, x='Estado', y=['Alcoholicos', 'Habitantes'],
                barmode='group', labels={'value': 'Cantidad'}, template='plotly_dark',
                title='Comparación de Alcohólicos y Habitantes por Estado mayores de 26 años')

    # Añadir una línea horizontal para la media de Alcohólicos por estado
    fig.add_hline(y=media_alcoholicos_estados, line_dash="dash", line_color="red",
                annotation_text=f'Media de Alcohólicos: {round(media_alcoholicos_estados)}',
                annotation_position="bottom right")

    st.plotly_chart(fig)





    # --------------------- Gráfico 2 - Gráfico circular de consumo promedio ---------------------
   



    mean_alcoholicos = df_nuevo2['Alcoholicos'].mean()
    mean_fumadores = df_nuevo2['Adictos_tabaco'].mean()
    mean_marihuana = df_nuevo2['Adictos_Marihuana'].mean()

    labels = ['Alcohólicos', 'Adictos Tabaco', 'Adictos Marihuana']
    sizes = [mean_alcoholicos, mean_fumadores, mean_marihuana]

    colors = {'Alcohólicos': 'gold', 'Adictos Tabaco': 'lightskyblue', 'Adictos Marihuana': 'lightcoral'}

    fig = px.pie(values=sizes, names=labels, color_discrete_map=colors, title='Porcentaje de adicciones')
    st.plotly_chart(fig)




    # --------------------- Gráfico 3- Regresión lineal ---------------------
  
    # --------------------- Gráfico 4- Tendencia de totales por año ---------------------
    st.write('')
    st.write('')

    df_nuevo2['Año'] = pd.to_datetime(df_nuevo2['Año'], format='%Y')
    datos_agrupados = df_nuevo2.groupby(df_nuevo2['Año'].dt.year).mean().reset_index()

    plt.figure(figsize=(10, 6))
    plt.plot(datos_agrupados['Año'], datos_agrupados['Alcoholicos'], marker='o', label='Total de Alcohólicos')
    plt.plot(datos_agrupados['Año'], datos_agrupados['Adictos_tabaco'], marker='o', label='Adictos Tabaco')
    plt.plot(datos_agrupados['Año'], datos_agrupados['Adictos_Marihuana'], marker='o', label='Adictos Marihuana')

    plt.title('Tendencia de totales por año')
    plt.xlabel('Año')
    plt.ylabel('Total de adictos')
    plt.grid(True)
    plt.gca().set_facecolor('lightgrey')
    plt.legend()

    st.pyplot(plt)

    st.write('')
    st.write('')

    # --------------------- Matriz de correlación 5 ---------------------
    st.write('')
    st.write('')

    correlation = df_nuevo2.drop(columns=['Año']).corr()
    st.write("Matriz de correlación:")
    
    st.write(correlation)

    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
    plt.xticks(color='white')
    plt.yticks(color='white')
    plt.title('Matriz de correlación')
    plt.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.25)
    plt.gca().set_facecolor('grey')

    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', transparent=True)
    plt.close()
    st.image(buf)

    st.write('')



        # Código para codificar la imagen en base64
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
         data = f.read()
        return base64.b64encode(data).decode()

    encoded_image = get_base64_of_bin_file("img/marihuana-01.png")

    # Mostrar la imagen con transparencia
    st.markdown(
        f"""
        <div style="opacity: 0.3;">
            <img src="data:image/png;base64,{encoded_image}" style="width:100%">
        </div>
        """,
        unsafe_allow_html=True
    )

    
    st.write('')

# ----------------- Código principal -----------------
if __name__ == '__main__':
    app()
