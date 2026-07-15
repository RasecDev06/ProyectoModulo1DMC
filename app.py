import streamlit as st
import numpy as np
import libreria_funciones as lf

st.title("Proyecto modulo 1 fundamentals")
st.sidebar.title("Parametros")

st.image("Python_logo.png")
st.sidebar.image("DMC.png")

modulo = st.sidebar.selectbox("Elija un modulo", ["Modulo listas", "Modulo array", "Modulo funciones"])

if modulo == "Modulo listas":

    valor_inicial = st.number_input("Ingrese el valor inicial", value=0)
    valor_final = st.number_input("Ingrese el valor final", value=1)
    lista_numerica = list(range(valor_inicial, valor_final))
    st.write(lista_numerica)

elif modulo == "Modulo array":
    st.write("Estas en el modulo de arreglos")

    limite_inferior = st.number_input("Ingrese el limite inferior", value=1200)
    limite_superior = st.number_input("Ingrese el limite superior", value=1250)
    cantidad_datos = st.number_input("Ingrese la cantidad de datos a crear", value=31)

    datos_produccion = np.random.randint(limite_inferior, limite_superior, cantidad_datos)
    st.write(datos_produccion)

    st.write("La produccion total es:", np.sum(datos_produccion))
    st.write("La produccion promedio es:", np.mean(datos_produccion))

else: 
    st.write("Estas en el modulo de funciones")
    
    principal = st.number_input("Ingrese el monto del prestamo", value=0)
    tasa_anual = st.number_input("Ingrese la tasa anual en decimal", value=0.10)
    anios = st.number_input("Ingrese el numero de años del prestamo", value=1)
    pagos_por_anio = st.number_input("Ingrese la cantidad de pagos por año", value=12)
    
    cuota = lf.cuota_prestamo(principal, tasa_anual, anios, pagos_por_anio)

    st.write("La cuota mensual de pago será:", cuota)

