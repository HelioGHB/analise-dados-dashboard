import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard", layout="wide")
st.title("Dashboard de Análise de Dados")

# Cria o componente para upload do arquivo 
uploaded_file = st.file_uploader("Escolha um arquivo CSV ou Excel", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("Arquivo carregado com sucesso!")

        # Visualização dos dados
        st.subheader("Visualização dos dados - Primeiras Linhas")
        st.dataframe(df.head())

        # Estatísticas
        st.subheader("Resumo Estatístico")
        st.write(df.describe())

        # Gráficos
        st.subheader("Construção dos Gráficos")

        colunas = df.columns.tolist()
        col_x = st.selectbox("Selecione o eixo X:", colunas)
        col_y = st.selectbox("Selecione o eixo Y:", colunas)
        tipo_grafico = st. selectbox("Tipo de gráfico:", ["Barras", "Linhas", "Dispersão"])

        if tipo_grafico == "Barras":
            fig = px.bar(df, x=col_x, y=col_y, title=f"{col_y} por {col_x}")
        elif tipo_grafico == "Linhas":
            fig = px.line(df, x=col_x, y=col_y, title=f"Evolução de {col_y} por {col_x}")
        else:
            fig = px.scatter(df, x=col_x, y=col_y, title=f"Dispersão entre {col_x} e {col_y}")

        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")

else:
    st.info("Aguardando o upload de um arquivo para iniciar a análise.")