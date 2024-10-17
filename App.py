# %% Importar Librerias
import pandas as pd
import streamlit as st
import plotly_express as px

# %% Cargando DB
df = pd.read_csv("vehicles_us.csv")

# %% Encabezado
st.header("Vehicles EDA")
st.write("Exploratory Data Analisis")

# %% Botones
btn_histograma = st.button("Construir Histograma")

# %%
if btn_histograma:
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
