import requests
import streamlit as st

api="https://www.omdbapi.com"
apikey="ed8084c4"

st.title("SEARCH MOVIE AND TV SHOW IN IMDB..😎")

search=st.text_input("Enter movie and tv name show to find:")

if st.button("Get"):
    if search:
        api_url = f"{api}?t={search}&apikey={apikey}"

        response = requests.get(api_url)
        
        if response.status_code==200:
            data=response.json()
            
            st.subheader("🎬 Movie Details:")
            st.write("Title :",data['Title'])
            st.write("Year :",data['Year'])
            st.write("Rated :",data['Rated'])
            st.write("Released :",data['Released'])
            st.write("Runtime :",data['Runtime'])
            st.write("Genre :",data['Genre'])
            st.write("imdbRating :",data['imdbRating'])
            st.image(data['Poster'],caption=data['Title'])
            
        else:
            st.error("❌ Movie not found. Please check the name and try again.")
    else:
        st.error("⚠️ Error fetching data from the OMDB API. Try again later.")
else:
    st.warning("🔎 Please enter a movie name to search.")