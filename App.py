# %%
# Importar Librerias
import pandas as pd
import streamlit as st
import plotly_express as px

# %% Cargando DB
df = pd.read_csv("notebooks/StudentsPerformance.csv")

# %%
# Ajustes
df = df[['gender', 'race/ethnicity',
         'lunch', 'preparation course', 'math', 'reading', 'writing']]

# %% Variables
tdf = df.copy()  # Copia del dataframe para actualizar con los botones

# %% Encabezado
st.header("Students Performance")
st.subheader("Exploratory Data Analysis")
st.write("___")
st.write("Dataset Sample")

# %%
# Separacion
st.dataframe(df.sample(5))

# Crear los checkboxes
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


# Crear y mostrar el histograma
fig = px.histogram(tdf, x=["math", "reading", "writing"])
st.plotly_chart(fig, use_container_width=True)

st.write("___")

st.write("How does the lunch affect the students results?")

cl1, cl2 = st.columns(2)
with cl1:
    tdf2 = df[df["lunch"] == 'standard']
    # Crear y mostrar el scatter plot
    fig = px.scatter_3d(tdf2, x="math", y="reading", z="writing", opacity=0.25)
    st.plotly_chart(fig, use_container_width=True)
with cl2:
    tdf2 = df[df["lunch"] == 'free/reduced']
    # Crear y mostrar el scatter plot
    fig = px.scatter_3d(tdf2, x="math", y="reading", z="writing", opacity=0.25)
    st.plotly_chart(fig, use_container_width=True)
