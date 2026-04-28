import streamlit as st
import pandas as pd
import requests
import os

st.title("⚽ Football Analytics")

# O Streamlit Cloud lê as chaves do menu "Secrets"
api_key = st.secrets.get("API_FOOTBALL_KEY")
tg_token = st.secrets.get("TELEGRAM_BOT_TOKEN")

st.write("Conectado à API com sucesso!" if api_key else "Configure a API Key nos Secrets.")

# Coloque aqui a lógica do seu painel e bot que criamos antes
if st.button("Listar Jogos de Hoje"):
    st.write("Buscando jogos...")
    # Aqui você pode chamar a função que criamos para listar os jogos
