# Importando as bibliotecas necessárias
import streamlit as st
import yfinance as yf
import pandas as pd

# APP page settings
st.set_page_config(
    menu_items={
    'Get Help': 'https://github.com/SidneyTeodoroJr',
    'Report a bug': "https://github.com/SidneyTeodoroJr/stock_performance",
    'About': "Contributions are welcome!"
    }
)

st.title("FINANCE DASHBOARD")
 
tickers = ("TSLA", "AAPL", "MSFT", "BTC-USD", "ETH-USD", "NVDA") # Lista de tickers

dropdown = st.multiselect("Pick your assets", tickers) # Menu

# Campos de entrada 
start = st.date_input("Start", value=pd.to_datetime("2020-01-01"))
end = st.date_input("End", value=pd.to_datetime("today"))

# Calcular os retornos relativos dos ativos 
def relativeret(df):
    rel = df.pct_change()               
    cumret = (1 + rel).cumprod() - 1    
    cumret = cumret.fillna(0)           
    return cumret


# Verifica se foi selecionado
if len(dropdown) > 0:
    df = relativeret(yf.download(dropdown, start, end)["Adj Close"]) # Baixa os dados 
    
    st.header("Returns of: {}".format(dropdown)) # Cabeçalho do gráfico
    
    data_frame = pd.DataFrame(df)
    st.dataframe(data_frame, use_container_width=True)

    st.line_chart(df)

    st.bar_chart(df)