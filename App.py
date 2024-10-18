# %%
# Importar Librerias
import pandas as pd
import streamlit as st
import plotly_express as px

# %% Cargando DB
# df = pd.read_csv("vehicles_us.csv")
lng = pd.read_csv("lenguage.csv")

# %% Variables
Lenguage: str = "English"
Histogram: bool = False
Scatter: bool = False

# %% Lenguage
esp, eng = st.columns(2)
with esp:
    btn_esp = st.button(lng.loc[1, Lenguage])
with eng:
    btn_heng = st.button(lng.loc[1, Lenguage])

# %%
print(lang.sample())

# %% Encabezado
st.header("Vehicles EDA")
st.write("Exploratory Data Analisis")
st.write("")
st.write("Dataset")
df


# %% Botones
col1, col2 = st.columns(2)
with col1:
    btn_histograma = st.button("Histogram")
with col2:
    btn_histograma = st.button("Scatter")

# %% Logica de los Botones
if btn_histograma:
    # crear un histograma
    fig = px.histogram(df, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    pass

# %%
