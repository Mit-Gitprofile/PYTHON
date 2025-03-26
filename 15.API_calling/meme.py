import requests
import streamlit as st

st.title("-------------------")
st.title("| 🌥️P-WEATHER APP |")
st.title("-------------------")

city = st.text_input("ENTER CITY NAME :")

api = f"http://www.omdbapi.com/?i=tt3896198&apikey=30fec5b4"


if st.button("🔍SEARCH") :
        response = requests.get(api)
        response.json()