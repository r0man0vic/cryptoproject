import streamlit as st
import yfinance as yf
st.set_page_config(page_title="Crypto Risks", layout="wide")
st.title("Crypto Risks")
coin = st.selectbox("Choose cryptocurrency",["BTC-USD", "ETH-USD"], index=0)
period = st.selectbox("Choose period",["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"],index=2)
data = yf.download(coin, period=period, progress=False)
data = data.dropna()
#btc = yf.download("BTC-USD", period="6mo", progress=False)
#st.line_chart(btc["Close"])
if not data.empty:
    st.line_chart(data["Close"])
else:
    st.warning("No data available")


#st.write("Version")