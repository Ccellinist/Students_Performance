# %%
# Importar Librerias
import pandas as pd
import streamlit as st
import plotly_express as px

# %% Cargando DB
df = pd.read_csv("notebooks/StudentsPerformance.csv")
lng = pd.read_csv("lng.csv")
lng = lng.set_index('message')

# %% Variables
Lenguage: str = "English"
Histogram: bool = False
Scatter: bool = False
chart_type: str = ""

# %%
# funcion para simplificar mensajes


def msg(message: str):
    return lng.loc[message, Lenguage]


# %% Lenguage
esp, eng = st.columns(2)
with eng:
    btn_eng = st.button('English')
with esp:
    btn_esp = st.button('Español')

if btn_esp:
    Lenguage = "Espanol"
if btn_eng:
    Lenguage = "English"

# %% Encabezado
st.header(msg('titulo'))
st.subheader(str(msg('mainmsg')))
st.write("___")
st.write(msg('tabla'))

# %%
# Sample
st.dataframe(df)


# %%
# Botón para histograma
col1, col2, col3 = st.columns(3)
with col1:
    btn_hist_1 = st.button(msg('btn_hist_mat'))
with col2:
    btn_hist_2 = st.button(msg('btn_hist_lec'))
with col3:
    btn_hist_3 = st.button(msg('btn_hist_esc'))

if btn_hist_1:
    # crear un histograma
    fig = px.histogram(df, x='math_score')
    st.plotly_chart(fig, use_container_width=True)
if btn_hist_2:
    # crear un histograma
    fig = px.histogram(df, x='reading_score')
    st.plotly_chart(fig, use_container_width=True)
if btn_hist_3:
    # crear un histograma
    fig = px.histogram(df, x='writing_score')
    st.plotly_chart(fig, use_container_width=True)
