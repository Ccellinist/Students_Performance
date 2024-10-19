# %%
# MODULE DOCSTRING
"""this is the main code for the web page"""
# %%
# IMPORTAR LIBRERIAS
import pandas as pd
import streamlit as st
import plotly_express as px

# %%
# CARGA DATABASE
df = pd.read_csv("notebooks/StudentsPerformance.csv")

# %%
# AJUSTES
# Toma solo las columnas más importantes
df = df[['gender', 'race/ethnicity',
         'lunch', 'preparation course', 'math', 'reading', 'writing']]

# %%
# VARIABLES
# Copia del dataframe para actualizar con los botones
tdf = df.copy()  # Copia del dataframe para actualizar con los botones

# %%
# ENCABEZADO
# Titulo
st.header("Students Performance")
# Subtitulo
st.subheader("Exploratory Data Analysis")
# Linea divisora
st.write("___")
# Texto demostrativo
st.write("Dataset Sample")

# %%
# MUESTRA DATASET
st.dataframe(df.sample(5))

# %%
# Crear los checkbox en una sola fila horizontal
c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    gropu_a = st.checkbox("Group A", value=True)
with c2:
    gropu_b = st.checkbox("Group B", value=True)
with c3:
    gropu_c = st.checkbox("Group C", value=True)
with c4:
    gropu_d = st.checkbox("Group D", value=True)
with c5:
    gropu_e = st.checkbox("Group E", value=True)

# %%
# FUNCION PERSONALIZADA


def update_df():
    """this function updates the dataframe viewed in the main page"""

    selection = []
    if gropu_a:
        selection.append('group A')
    if gropu_b:
        selection.append('group B')
    if gropu_c:
        selection.append('group C')
    if gropu_d:
        selection.append('group D')
    if gropu_e:
        selection.append('group E')

    # Filtrar el DataFrame según la selección de checkboxes
    temporal_df = df[df['race/ethnicity'].isin(selection)]

    return temporal_df


# %%
# ACTUALIZAR
# Actualizar el DataFrame filtrado
tdf = update_df()

# %%
# MUESTRA EL HISTOGRAMA
fig = px.histogram(tdf, x=["math", "reading", "writing"])
st.plotly_chart(fig, use_container_width=True)

# Termina el histograma con una linea divisora
st.write("___")

# %%
# MUESTRA LOS DIAGRAMAS DE DISPERSION
st.write("How does the lunch affect the students results?")

cl1, cl2 = st.columns(2)
with cl1:
    tdf2 = df[df["lunch"] == 'standard']
    fig = px.scatter_3d(tdf2, x="math", y="reading", z="writing", opacity=0.25)
    st.plotly_chart(fig, use_container_width=True)
with cl2:
    tdf2 = df[df["lunch"] == 'free/reduced']
    fig = px.scatter_3d(tdf2, x="math", y="reading", z="writing", opacity=0.25)
    st.plotly_chart(fig, use_container_width=True)
