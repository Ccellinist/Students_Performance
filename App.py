# %%
# Importar Librerias
import pandas as pd
import streamlit as st
import plotly_express as px

# %% Cargando DB
df = pd.read_csv("notebooks/StudentsPerformance.csv")

# %%
# Ajustes
df = df[['race/ethnicity', 'math', 'reading', 'writing']]

# %% Variables
tdf = df.copy()  # Copia del dataframe para actualizar con los botones

# %% Encabezado
st.header("Students Performance")
st.subheader("Exploratory Data Analysis")
st.write("___")
st.write("Dataset Sample")

# %%
# Separacion
tabla, checkbox = st.columns([5, 1])

# Crear los checkboxes
with checkbox:
    gropu_a = st.checkbox("Group A", value=True)
    gropu_b = st.checkbox("Group B", value=True)
    gropu_c = st.checkbox("Group C", value=True)
    gropu_d = st.checkbox("Group D", value=True)
    gropu_e = st.checkbox("Group E", value=True)

# Función para actualizar el DataFrame basado en los checkboxes seleccionados


def update_df():
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
    tdf = df[df['race/ethnicity'].isin(selection)]

    return tdf


# Actualizar el DataFrame filtrado
tdf = update_df()

# Mostrar el DataFrame filtrado en la columna 'tabla'
with tabla:
    st.dataframe(tdf.sample(5))

hist, scat = st.columns(2)
with hist:
    # Crear y mostrar el histograma
    fig = px.histogram(tdf, x=["math", "reading", "writing"])
    st.plotly_chart(fig, use_container_width=True)
with scat:
    # Crear y mostrar el scatter plot
    fig = px.scatter_3d(tdf, x="math", y="reading",
                        z="writing", opacity=0.25)
    st.plotly_chart(fig, use_container_width=True)

st.write("___")
