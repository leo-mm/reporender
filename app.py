import pandas as pd
import plotly.express as px
import streamlit as st

# Título
st.title("Análise de Dados de Veículos Usados")

# Carregar os dados
car_data = pd.read_csv("vehicles.csv")

# Opção para selecionar o gráfico
opcao = st.radio(
    "Selecione o gráfico que deseja visualizar:",
    ("Histograma da Quilometragem", "Dispersão Preço vs Quilometragem")
)

# Mostrar o gráfico conforme a seleção
if opcao == "Histograma da Quilometragem":
    st.write("Criando um histograma para a quilometragem dos veículos")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig)

elif opcao == "Dispersão Preço vs Quilometragem":
    st.write("Criando gráfico de dispersão entre preço e quilometragem")
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2)
