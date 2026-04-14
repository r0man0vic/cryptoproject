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
                  {"date":"2017-09-26","title":"First BTC Boom (2017)","description":"In 2017 crypto hasn't yet been mainstream, It was only beginning of the hype that crypto will create. In January 2017, Bitcoin was trading at approximately 1,000\$. By December of the same year, it skyrocketed to an unprecedented 20,000\$. That was an astounding 2,000% increase in just 12 months, marking Bitcoin's first all-time high. Bitcoin's appeal transcended the realm of tech enthusiasts and hackers in 2017. (For the first time, it was considered a legitimate financial asset in everyday life and became the main currency in darkweb, because of its anonymity and convinience of usage). Fear of missing out was a key driver of the 2017 bull run. As Bitcoin's price surged, retail investors rushed to buy in, fearing they would miss the opportunity to profit. The buying frenzy pushed prices even higher.","window":81,"image":"pics/2017.jpg"},
                  {"date":"2020-12-20","title":'BTC is called "digital gold" (2020-2021)',"description":'Two significant figures in business Ray Dalio and Stanley Druckenmiller called Bitcoin "Digital Gold" and said, that its a good investment, Stanley Druckenmiller even said that he holds some. Those statements from significant people caused increased intrests from regular people and investors, and thus price growth',"window":90,"image":"pics/gold.jpg"},
                  {"date":"2021-9-13","title":"Recovery after crysis (2021)","description":"Following the massive China mining ban in May/June 2021, the network's hash rate recovered, signaling a stabilization of the mining industry. (Hashrate recovery is the increase in total computational power used to mine crypto like Bitcoin, after a significant drop, indicating miners are returning online and the network is strengthening). And some minor factors like El Salvador Adoption: In September 2021, El Salvador became the first country to adopt Bitcoin as legal tender, bringing significant positive attention to the asset, and First Futures ETF: The launch of the first Bitcoin futures ETF made it easier for institutional investors to gain exposure to Bitcoin, increasing demand and driving prices higher.","window":55,"image":"pics/2021.jpg"},
                  {"date":"2023-12-15","title":"Investments inflow (2023-2024)","description":"Between September 2023 and March 2024, Bitcoin grew from roughly 27,000/$ to over 70,000/$ driven primarily by the approval of 10 US spot Bitcoin ETFs, anticipation of the April 2024 halving, and increased institutional adoption. Massive inflows into ETFs created supply scarcity, which, combined with maturing market cycles and reduced volatility, fueled the bullish rally.","window":90,"image":"pics/2024.jpg"},
                  {"date":"2024-11-1","title":"Stabillity period (2024)","description":"Bitcoin continued to rise as strong institutional demand and sustained capital inflows increased market confidence. At the same time, improving macroeconomic conditions, including expectations of lower interest rates, encouraged investors to allocate more capital into risk assets. Overall, increased market stability strengthened investor confidence, leading to greater investment and continued price growth.","window":45,"image":"pics/2024v2.jpg"},
                  {"date":"2025-05-31","title":"Consolidation Phase (2025) + Growth Conclusion","description":"Between April and July 2025, Bitcoin moved through a consolidation phase as the market stabilized after previous gains. Continued institutional demand supported prices, while broader macroeconomic conditions influenced investor behavior, leading to more gradual and controlled price movement. CONCLUSION About GROWTHS Of BTC: Bitcoin growth is primarily driven by strong market sentiment and investor hype, pretty much always amplified during periods of global stability. When economic conditions are stable and uncertainty is low, investor confidence increases, leading to greater demand and sustained upward price movement.","window":52,"image":"pics/2025.jpg"}],
        "Crash":[
                {"date":"2018-04-16","title":"Bubble burst (2018)","description":"Bitcoin crashed after the 2017 boom as the speculative bubble burst, with hype collapsing and panic selling driving prices sharply lower.","window":120,"image":"pics/bear.jpg"},
                {"date":"2020-02-18","title":"COVID-19 Market Crash (2020)","description":"Bitcoin dropped sharply as the COVID-19 pandemic triggered global panic across financial markets, causing investors to sell risk assets and move into safer positions.","window":29,"image":"pics/covid.jpg"},
                {"date":"2021-05-19","title":"China mining ban + Elon Musk tweets (2021)","description":"China’s mining crackdown and macro uncertainty triggered a sharp correction after a historic bull run. Elon Musk's tweets regarding energy concerns","window":36,"image":"pics/china.jpg"},
                {"date":"2021-12-18","title":"Federal Reserve tightening (2021-2022)","description":"Bitcoin declined as the Federal Reserve signaled tighter monetary policy, reducing liquidity and pushing investors away from risk assets.","window":35,"image":"pics/federal.jpg"},
                {"date":"2022-05-8","title":"Crash of Terra coin (2022)","description":"Bitcoin declined sharply as the collapse of the Terra ecosystem triggered widespread panic across the crypto market, leading to massive liquidations and loss of confidence. At the same time, tightening monetary policy reduced overall liquidity, adding additional pressure on risk assets and accelerating the sell-off.","window":40,"image":"pics/terra.jpg"},
                {"date":"2025-02-16","title":"Tariffs affect BTC (2025)","description":"The announcement of 25% tariffs on Canada and Mexico, and 10% on China by the U.S. administration, created severe volatility. These tariffs sparked fears of a global economic slowdown, pushing investors away from risky assets like Bitcoin and into safer havens.","window":22,"image":"pics/new.jpg"},
                {"date":"2026-01-25","title":"U.S Government Shutdown (2025)","description":'The government shutdown, which was considered the longest in US history, caused the Treasury General Account (TGA) to swell, locking up liquidity in the federal vault and starving risk assets like crypto. Investors pulled back from riskier assets, with market analysts noting a shift towards "profit-taking" and "de-risking" while waiting for economic data, which was delayed by the shutdown.',"window":11,"image":"pics/possible.jpg"},
                {"date":"2026-03-6","title":"World Tension (2025-2026) + Crash Conclusion","description":"Bitcoin faced volatility as global tensions reduced investor confidence, creating a risk-off environment and increasing selling pressure, because of the unstable situation in today's world. CONCLUSION About CRASHES Of BTC: Bitcoin crashes are more complex and typically driven by multiple factors rather than a single event. Major declines often occur when speculative bubbles fueled by hype burst, triggering panic selling. External shocks such as global crises like COVID-19 can also impact the market by increasing uncertainty and reducing demand for risk assets. Regulatory actions, including mining bans in major countries like China, disrupt the ecosystem and weaken confidence. Market sentiment can be further influenced by public statements from influential figures, while macroeconomic factors such as monetary tightening or government instability reduce liquidity and increase risk-off behavior. In addition, the collapse of major crypto projects can create contagion across the market. Overall, global tensions and uncertainty remain a key underlying force, as they consistently reduce investor confidence and contribute to downward pressure on Bitcoin prices.","window":150,"image":"pics/final.jpg"}
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


#st.write("3")