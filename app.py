import streamlit as st
import pandas as pd
from tools import scrape_market_news

st.set_page_config(page_title="CognitiveAgentX Dashboard", layout="wide")

st.title("🤖 CognitiveAgentX Analytics Dashboard")
st.caption("Real-time data aggregation and intelligence pipeline")

# Sidebar Configuration
st.sidebar.header("Control Panel")
target_topic = st.sidebar.text_input("Enter Research Topic:", value="Artificial Intelligence")

if st.sidebar.button("Execute Data Stream"):
    st.subheader(f"📊 Real-time Stream Results for: {target_topic}")
    
    with st.spinner("Fetching underlying structural live data..."):
        try:
            raw_headlines = scrape_market_news(target_topic)
            headline_list = raw_headlines.split(" | ")
            
            # Formatting data framework into an active UI table
            df = pd.DataFrame({
                "Index": range(1, len(headline_list) + 1),
                "Aggregated News Headlines": headline_list
            })
            
            st.dataframe(df, use_container_width=True)
            st.success("Data parsing pipeline fully completed.")
            
        except Exception as e:
            st.error(f"Pipeline connectivity issue: {e}")