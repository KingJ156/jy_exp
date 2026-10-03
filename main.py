import streamlit as st 
import requests

BASE_URL = "https://science.nasa.gov/wp-json/wp/v2/apod-basic/?api_key=DEMO_KEY" 

def fetch_apod(date, timeout: float = 6):

    date = str(date)
    date = date.replace("-", "")
    date = date[2:]

    final_URL = BASE_URL + "/" + date

    r = requests.get(
        final_URL,
        params={"api_key": "DEMO_KEY"},
        timeout=timeout
    )

    r.raise_for_status()

    return r.json()


st.title("Space")


date = st.date_input("Date")

st.write(date)

if st.button("Show picture"):

    ans = fetch_apod(date)

    st.write("Title:", ans["title"])
    st.write("Explanation:", ans["explanation"])

    st.image(ans["hdurl"])