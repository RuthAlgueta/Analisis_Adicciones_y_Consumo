import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from streamlit_option_menu import option_menu
import sklearn
from sklearn.metrics import classification_report, roc_curve, auc, confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier 
import numpy as np
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import base64


def app():
    # Carga del df
    drogas = pd.read_csv("C:/Users/rutha/Desktop/SAMPLEREPO/03_Modulo_3/7_proyecto_Final/data/limpio_drugs_and_riskfactors.csv")
    
    
    #st.title('Simulador de Exposición a Drogas💊')
    
 # Texto con cubo



    container = st.container()
    with container:
        st.markdown(
                """
                        <div style='background-color: #FFA07A; border-radius: 10px; padding: 20px; text-align: center; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3); margin-top: 10px; margin-left: auto; margin-right: auto; width: fit-content;'>
                        <div style='font-size: 30px; font-weight: 700; margin-bottom: 15px; color: #ffffff;'>Simulador de Exposición a Drogas💊</div>
                        </div>
                        """,
                                unsafe_allow_html=True
         )
        
        st.title(' ')

        titulo_html = """
                <h1 style='text-align: center; color: white; font-size: 25px;'>
                        Puede ajustar los siguientes parámetros que encuentra en este formulario:
                </h1>
                """
        st.markdown(titulo_html, unsafe_allow_html=True)




            # Creando sliders/selectboxes para las entradas de las variables categoricas

    td = st.selectbox("Drogas", ("Alcohol", "Tabaco", "Cocaina", "Crack", "Heroina", "Marihuana", "Metanfetamina", "Analgésicos"))                                   
    edad = st.selectbox("edad", ("De 12 a 17 años", "De 18 a 25 años", "De 26 a 34 años", "De 35 a 49 años", "De 50 a 64 años", "65 años o más"))
    Educación = st.selectbox("Educación", ("No graduado de la secundaria", "Graduado de la secundaria", "Algo de universidad, o título de asociado", "Graduado universitario", "De 12 a 17 años"))
    Empleo = st.selectbox("Empleo", ("El participante está empleado a tiempo completo", "El participante está empleado a tiempo parcial", "El participante está desempleado", "Otro (incl. no en la fuerza laboral)", "El participante es menor de edad; de 12 a 14 años"))
    Convivencia_Padre = st.selectbox("Convivencia_Padre", ("Sí, el padre está en el hogar", "No, el padre no está en el hogar", "No sabe si el padre está presente o no", "el participante tiene 18 años o más"))
    Convivencia_Madre = st.selectbox("Convivencia_Madre", ("Sí, la madre está en el hogar", "No, la madre no está en el hogar", "No sabe si la madre está presente o no", "el participante tiene 18 años o más"))
    Ingresos = st.selectbox("Ingresos", ("Menos de $20,000", "Entre $20,000 y $49,000", "Entre $50,000 y $74,999", "Más de $75,000"))	
    Raza = st.selectbox("Raza", ("Blanco", "Negro", "Nativo Americano", "Nativo Hawaiano/Islas del Pacífico", "Asiático", "Multirracial", "Hispano"))
    Género = st.selectbox("Género", ("El participante es masculino", "El participante es femenino"))
        
    # Preprocesamiento de datos
    drogas = drogas.dropna()
    X = drogas[["edad", "Educación", "Empleo", "Convivencia_Padre", "Ingresos", "Convivencia_Madre", "Raza", "Género"]]
    y = drogas[td]





    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(max_depth=4, random_state = 10) 
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy_score(y_test,y_pred)

        # funcion para devolver los datos introducidos (intrfaz usuario) al modelo (interfaz maquina)

    def prediction(edad, Educación, Empleo, Convivencia_Padre, Ingresos, Convivencia_Madre,Raza,Género):
            # Pre procesamiento
            # Is_female
        if	edad == "De 12 a 17 años":
                edad = 1
        if	edad == "De 18 a 25 años":
                edad = 2 
        if	edad == "De 26 a 34 años":
                edad = 3 
        if	edad == "De 35 a 49 años":
                edad = 4 
        if	edad == "De 50 a 64 años":
                edad = 5 
        if	edad == "65 años o más":
                edad = 6 
                
        if	Educación == "No graduado de la secundaria":
                Educación = 1
        if	Educación == "Graduado de la secundaria":
                Educación = 2 
        if	Educación == "Algo de universidad, o título de asociado":
                Educación = 3 
        if	Educación == "Graduado universitario":
                Educación = 4 
        if	Educación == "De 12 a 17 años":
                Educación = 5 
                
        if	Empleo == "El participante está empleado a tiempo completo":
                Empleo = 1
        if	Empleo == "El participante está empleado a tiempo parcial":
                Empleo = 2 
        if	Empleo == "El participante está desempleado":
                Empleo = 3 
        if	Empleo == "Otro (incl. no en la fuerza laboral)":
                Empleo = 4 
        if	Empleo == "El participante es menor de edad; de 12 a 14 años":
                Empleo = 99 
            
        if	Convivencia_Padre == "Sí, el padre está en el hogar":
                Convivencia_Padre = 1
        if	Convivencia_Padre == "No, el padre no está en el hogar":
                Convivencia_Padre = 2 
        if	Convivencia_Padre == "No sabe si el padre está presente o no":
                Convivencia_Padre = 3 
        if	Convivencia_Padre == "el participante tiene 18 años o más":
                Convivencia_Padre = 4 
            
                
        if	Convivencia_Madre == "Sí, la madre está en el hogar":
                Convivencia_Madre = 1
        if	Convivencia_Madre == "No, la madre no está en el hogar":
                Convivencia_Madre = 2 
        if	Convivencia_Madre == "No sabe si la madre está presente o no":
                Convivencia_Madre = 3 
        if	Convivencia_Madre == "el participante tiene 18 años o más":
                Convivencia_Madre = 4 
            
        if	Ingresos == "Menos de $20,000":
                Ingresos = 1
        if	Ingresos == "Entre $20,000 y $49,000":
                Ingresos = 2 
        if	Ingresos == "Entre $50,000 y $74,999":
                Ingresos = 3 
        if	Ingresos == "Más de $75,000":
                Ingresos = 4 
                
        if	Raza == "Blanco":
                Raza = 1
        if	Raza == "Negro":
                Raza = 2 
        if	Raza == "Nativo Americano":
                Raza = 3 
        if	Raza == "Nativo Hawaiano/Islas del Pacífico":
                Raza = 4 
        if	Raza == "Asiático":
                Raza = 5 
        if	Raza == "Multirracial":
                Raza = 6 
        if	Raza == "Hispano":
                Raza = 7 
                
        if	Género == "El participante es masculino":
                Género = 1
        if	Género == "El participante es femenino":
                Género = 2 
        
            # Hacemos predicción
        pred = model.predict([[edad, Educación, Empleo, Convivencia_Padre, Ingresos, Convivencia_Madre,Raza,Género]])
            #if pred == 0:
            #    pred = "No consumes alcohol"
            #else:
            #    pred = "Consumes alcohol"
        return pred
    

    
    st.title(' ')
  #-----------------------------------------------contenedor de titulos ---------------------------

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
                        Averigua sí el usuario consume la droga según las variables seleccionadas
                </h1>
                """
            st.markdown(titulo_html, unsafe_allow_html=True)

                



    #-------------------- -----------------------Botónes de predicción-----------------------------------------
        


    st.title(' ')
    if st.button("Predecir"):
        result = prediction(edad, Educación, Empleo, Convivencia_Padre, Ingresos, Convivencia_Madre, Raza, Género)
        st.write(f'droga seleccionada: {td}')
        # Mostrar resultado de la predicción
        if result[0] == 0:
            st.success("según las variables seleccionadas no consumes la droga indicada")
        else:
            st.warning("según las variables seleccionadas sí consumes la droga indicada")

    # Cálculo del porcentaje de aciertos
    def calcular_porcentaje_aciertos():
        y_pred = model.predict(X_test)
        precision = accuracy_score(y_test, y_pred)
        return precision

    # Botón para calcular y mostrar el porcentaje de aciertos
    if st.button('Calcular Porcentaje de Aciertos del Modelo RandomForest '):
        porcentaje_aciertos = calcular_porcentaje_aciertos()
        st.write(f'El porcentaje de aciertos del modelo RandomForest de {td} es : {porcentaje_aciertos:.2%}')



    # Configurar la opción para deshabilitar la advertencia
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Calculamos la matriz de confusión
    cm = confusion_matrix(y_test, y_pred)

    # Función para mostrar la matriz de confusión
    def mostrar_matriz_confusion():
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, cmap='Blues', fmt='g', cbar=False)
        plt.xlabel('Clase Predicha')
        plt.ylabel('Clase Real')
        plt.title('Matriz de Confusión')
        st.pyplot()

    # Interfaz de usuario
    # st.title('Visualización de la Matriz de Confusión')

    if st.button('Mostrar Matriz de Confusión'):
        mostrar_matriz_confusion()




# Código para codificar la imagen en base64
    def get_base64_of_bin_file(bin_file):
      with open(bin_file, 'rb') as f:
        data = f.read()
      return base64.b64encode(data).decode()

    encoded_image = get_base64_of_bin_file("img/adicciones-01.png")

# Mostrar la imagen con transparencia
    st.markdown(
     f"""
    <div style="opacity: 0.5;">
        <img src="data:image/png;base64,{encoded_image}" style="width:100%">
    </div>
    """,
    unsafe_allow_html=True
)


   

    if __name__ == "__main__":
        main()

# Ejecuta la app
if __name__ == "__main__":
    app()