import streamlit as st
import yfinance as yf
import pandas as pd
st.set_page_config(page_title="Crypto Risks", layout="wide")
st.title("Bitcoin Currency Growth and Crash Drivers")
st.set_page_config(page_title="Crypto",layout="wide")
st.title("Project by Mikhail")
'''
The application includes two types of events: “Growth” and “Crash”. Users can select an event to explore what happened during that period and see its impact on the all-time Bitcoin price chart.
'''
mode = st.radio("Choose Event type, either ones, that affected Growth of Crash of BTC", ["Growth","Crash"], horizontal=True)
coin="BTC-USD"
#period = st.selectbox("Choose period",["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"],index=2)
#data = yf.download(coin, period=period, progress=False)
#data = data.dropna()
#btc = yf.download("BTC-USD", period="6mo", progress=False)
#st.line_chart(btc["Close"])
events={"Growth":[
                  {"date":"2017-09-26","title":"First BTC Boom (2017)","description":"In 2017 crypto hasn't yet been mainstream, It was only beginning of the hype that crypto will create. In January 2017, Bitcoin was trading at approximately 1,000\$. By December of the same year, it skyrocketed to an unprecedented 20,000\$. That was an astounding 2,000% increase in just 12 months, marking Bitcoin's first all-time high (ATH). Bitcoin's appeal transcended the realm of tech enthusiasts and hackers in 2017. For the first time, it was considered a legitimate financial asset and a store of value. Fear of missing out (FOMO) was a key driver of the 2017 bull run. As Bitcoin's price surged, retail investors rushed to buy in, fearing they would miss the opportunity to profit. The buying frenzy created a feedback loop, pushing prices even higher.","window":81,"image":"pics/2017.jpg"},
                  {"date":"2020-12-20","title":'BTC is called "digital gold" (2020-2021)',"description":'Two significant figures in business Ray Dalio and Stanley Druckenmiller called Bitcoin "Digital Gold" and said, that its a good investment, Stanley Druckenmiller even said that he holds some. Those statements from significant people caused increased intrests from regular people and investors, and thus price growth',"window":90,"image":"pics/gold.jpg"},
                  {"date":"2021-9-13","title":"Recovery after crysis (2021)","description":"Following the massive China mining ban in May/June 2021, the network's hash rate recovered, signaling a stabilization of the mining industry. Hashrate recovery is the increase in total computational power used to mine crypto like Bitcoin, after a significant drop, indicating miners are returning online and the network is strengthening. And some minor factors like El Salvador Adoption: In September 2021, El Salvador became the first country to adopt Bitcoin as legal tender, bringing significant positive attention to the asset, and First Futures ETF: The launch of the first Bitcoin futures ETF made it easier for institutional investors to gain exposure to Bitcoin, increasing demand and driving prices higher.","window":55,"image":"pics/2021.jpg"},
                  {"date":"2023-12-15","title":"2024","description":"gazz","window":90,"image":"pics/2024.jpg"},
                  {"date":"2024-11-1","title":"2024v2","description":"gazz","window":45,"image":"pics/2024v2.jpg"},
                  {"date":"2025-05-31","title":"2025","description":"gazz","window":52,"image":"pics/2025.jpg"}],
        "Crash":[
                {"date":"2018-04-16","title":"Bear market in 2017","description":"The 2017 bull run created massive speculation. When the bubble popped, the entire crypto market entered a deep bear cycle.","window":120,"image":"pics/bear.jpg"},
                {"date":"2020-02-18","title":"Covid-19 crypto crisis","description":"global pandemic","window":29,"image":"pics/covid.jpg"},
                {"date":"2021-05-19","title":"China mining ban + Elon Musk tweets ","description":"China’s mining crackdown and macro uncertainty triggered a sharp correction after a historic bull run. Elon Musk's tweets regarding energy concerns","window":36,"image":"pics/china.jpg"},
                {"date":"2021-12-18","title":"Federal Reserve tightening","description":"Bitcoin declined as the Federal Reserve signaled tighter monetary policy, reducing liquidity and pushing investors away from risk assets.","window":35,"image":"pics/federal.jpg"},
                {"date":"2022-05-8","title":"Terra crash","description":"Terra collapsed","window":40,"image":"pics/terra.jpg"},
                {"date":"2025-02-16","title":"2025","description":"Terra collapsed","window":22,"image":"pics/new.jpg"},
                {"date":"2026-01-25","title":"Possible gov shutdown","description":"uncertanty","window":11,"image":"pics/possible.jpg"},
                {"date":"2026-03-6","title":"world tension","description":"4 oct 2025- 22nov 2025","window":150,"image":"pics/final.jpg"},
                ]}
eventlist=events[mode]
if eventlist:
    eventtitle=[e["title"] for e in eventlist]
    exactevent=st.selectbox("Select event",eventtitle)
    event_data=next(e for e in eventlist if e["title"]==exactevent)
if event_data:
    center=pd.to_datetime(event_data["date"])
    window=event_data.get("window",15)
    start=(center-pd.Timedelta(days=window)).strftime("%Y-%m-%d")
    end=(center+pd.Timedelta(days=window)).strftime("%Y-%m-%d")
    data=yf.download(coin,start=start,end=end,progress=False)
    data=data.dropna()
#button
jump_days=1

#if st.button("Jump to time") and event_data:
#    center=pd.to_datetime(event_data["date"])
#    window=event_data.get("window",15)
   # start=(center-pd.Timedelta(days=window)).strftime("%Y-%m-%d")
 #   end=(center+pd.Timedelta(days=window)).strftime("%Y-%m-%d")
  #  data=yf.download(coin,start=start,end=end,progress=False)
  #  data=data.dropna()

if not data.empty:
    st.line_chart(data["Close"])

if event_data:
    st.subheader(event_data["title"])

    if event_data and "image" in event_data:
        st.image(event_data["image"],use_container_width=True)

    st.write(event_data["description"])


#st.write("2")