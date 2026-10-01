import streamlit as st 
import requests

BASE_URL = "https://science.nasa.gov/wp-json/wp/v2/apod-basic/?api_key=DEMO_KEY" 

def fetch_apod(timeout: float = 6) -> dict:
    r = requests.get(BASE_URL, timeout=timeout)
    r.raise_for_status()
    return r.json()
st.title("Space")

ans =  fetch_apod()
st.write(ans)