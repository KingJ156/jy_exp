import streamlit as st 
import requests

BASE_URL = "https://science.nasa.gov/wp-json/wp/v2/apod-basic/?api_key=DEMO_KEY" 

def fetch_apod(timeout: float = 6):
    r = requests.get(BASE_URL, timeout=timeout)
    r.raise_for_status()
    return r.json()


st.title("Space")

ans = fetch_apod()



apod = ans[0]

st.write("Title:", apod["title"])
if st.button("Show Date"):
    st.write("Date:", ans[0]["date"])
st.write("Explanation:", apod["explanation"])
st.write("Credit:", apod["credit"])
st.image(apod["hdurl"])