import streamlit as st
import yfinance as yf
st.set_page_config(page_title="Crypto",layout="wide")
st.title("Crypto Drop/Growth")
mode = st.radio("Choose growth or drop of crypto currency", ["Growth","Drop"], horizontal=True)
coin = st.selectbox("Choose cryptocurrency",["BTC-USD", "ETH-USD"], index=0)
period = st.selectbox("Choose period",["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"],index=2)
data = yf.download(coin, period=period, progress=False)
data = data.dropna()
events={"Growth":[],"Drop":[{"date":"","title":"Ms sells btc","description":"jhebcheb"},{"date":"2022-11-09","title":"FTX Collapse","description":"ms promised not to sell etc, but they did"}]}
eventlist=events[mode]
if eventlist:
    eventtitle=[e["title"] for e in eventlist]
    exactevent=st.selectbox("Select event",eventtitle)
    event_data=next(e for e in eventlist if e["title"]==exactevent)
else:
    event_data=None
if not data.empty:
    st.line_chart(data["Close"])
else:
    st.warning("No data available")


#st.write("1.0")