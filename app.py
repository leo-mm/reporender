import pandas as pd
import plotly.express as px
import streamlit as st

# Cabeçalho do aplicativo
st.header('Análise de Dados de Veículos Usados')

# Carregar o conjunto de dados
car_data = pd.read_csv("vehicles.csv")

# Botão para criar o histograma
hist_button = st.button('Criar histograma')

if hist_button:
    # Mensagem ao clicar no botão
    st.write('Criando um histograma para a quilometragem dos veículos')

    # Criar o histograma
    fig = px.histogram(car_data, x='odometer', nbins=30,
                        title='Distribuição da Quilometragem dos Veículos')

    # Exibir o histograma no aplicativo
    st.plotly_chart(fig, use_container_width=True)
