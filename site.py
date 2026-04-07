import streamlit as st
import yfinance as yf
import pandas as pd
st.set_page_config(page_title="Crypto Risks", layout="wide")
st.title("Crypto Risks")
st.set_page_config(page_title="Crypto",layout="wide")
st.title("Crypto Drop/Growth")
mode = st.radio("Choose growth or drop of crypto currency", ["Growth","Drop"], horizontal=True)
coin = st.selectbox("Choose cryptocurrency",["BTC-USD", "ETH-USD"], index=0)
period = st.selectbox("Choose period",["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"],index=2)
data = yf.download(coin, period=period, progress=False)
data = data.dropna()
#btc = yf.download("BTC-USD", period="6mo", progress=False)
#st.line_chart(btc["Close"])
events={"Growth":[{"date":"2020-12-10","title":"digital gold","description":"gazz","window":90}],
        "Drop":[
                {"date":"2020-03-10","title":"Covid-19 crypto crisis","description":"global pandemic","window":30},
                {"date":"2018-04-16","title":"Bear market in 2017","description":"The 2017 bull run created massive speculation. When the bubble popped, the entire crypto market entered a deep bear cycle.","window":120},
                {"date":"2021-05-15","title":"China mining ban + Elon Musk tweets ","description":"China’s mining crackdown and macro uncertainty triggered a sharp correction after a historic bull run. Elon Musk's tweets regarding energy concerns","window":50},
                {"date":"2022-05-4","title":"Terra crash","description":"Terra collapsed","window":45},
                {"date":"2021-12-18","title":"Federal Reserve tightening","description":"Bitcoin declined as the Federal Reserve signaled tighter monetary policy, reducing liquidity and pushing investors away from risk assets.","window":35},
                #{"date":"2025-02-15","title":"Trump's tariffs","description":"1 feb -1march 2025Trump's announcement on new tarriffs","window":55},
                {"date":"2026-03-6","title":"world tension","description":"4 oct 2025- 22nov 2025","window":150},
                {"date":"2026-02-4","title":"Possible gov shutdown","description":"uncertanty","window":22}]}
#{"date":"20-11-09","title":"FTX Collapse","withdrawals around the world":"ms promised not to sell etc, but they did"}]}
eventlist=events[mode]
if eventlist:
    eventtitle=[e["title"] for e in eventlist]
    exactevent=st.selectbox("Select event",eventtitle)
    event_data=next(e for e in eventlist if e["title"]==exactevent)
#button
jump_days=1

if st.button("Jump to time") and event_data:
    center=pd.to_datetime(event_data["date"])
    window=event_data.get("window",15)
    start=(center-pd.Timedelta(days=window)).strftime("%Y-%m-%d")
    end=(center+pd.Timedelta(days=window)).strftime("%Y-%m-%d")
    data=yf.download(coin,start=start,end=end,progress=False)
    data=data.dropna()
else:
    event_data=None
if not data.empty:
    st.line_chart(data["Close"])
if event_data:
    st.subheader(event_data["title"])
 #   st.caption(event_data["date"])
    st.write(event_data["description"])
#else:
#    st.warning("No data available")


#st.write("2v")