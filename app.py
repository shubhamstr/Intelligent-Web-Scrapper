import streamlit as st
from scrapers.trek_scraper import scrape_events
import pandas as pd

st.title("Web Scraping with Streamlit")
st.write("My first Streamlit app")

events = scrape_events()
st.write("events")
st.write(events)

df = pd.DataFrame(events)

st.dataframe(df)