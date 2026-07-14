import streamlit as st
st.title("Proyecto modulo 1 fundamentals")
st.sidebar.title("Parametros")

st.image("Python_logo.png")
st.sidebar.image("DMC.png")

valor_inicial = st.number_input("Ingrese el valor inicial", value=0)
valor_final = st.number_input("Ingrese el valor final", value=1)

lista_numerica = list(range(valor_inicial, valor_final))

st.write(lista_numerica)
