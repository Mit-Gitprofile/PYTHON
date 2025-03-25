

import requests
import streamlit as st

# Set the title of the Streamlit app
st.title("OMDB Movie Finder")

# OMDB API key (replace with your actual key if necessary)
api_key = "ed8084c4"
base_url = "https://www.omdbapi.com/"

# Input field for the movie name
movie = st.text_input("Enter Movie Name to Find:")

# When the user clicks the "Submit" button
if st.button("Submit"):
    if movie:
        # Prepare the API URL with user input
        api_url = f"{base_url}?t={movie}&apikey={api_key}"

        # Fetch data from OMDB API
        response = requests.get(api_url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Check if the movie is found
            if data.get("Response") == "True":
                st.subheader("🎬 Movie Details:")
                st.write(f"**Title:** {data['Title']}")
                st.write(f"**Year:** {data['Year']}")
                st.write(f"**Genre:** {data['Genre']}")
                st.write(f"**Director:** {data['Director']}")
                st.write(f"**Actors:** {data['Actors']}")
                st.write(f"**Plot:** {data['Plot']}")
                st.write(f"**IMDb Rating:** {data['imdbRating']}")

                # Display movie poster if available
                if "Poster" in data and data["Poster"] != "N/A":
                    st.image(data["Poster"], caption=data['Title'])
            else:
                st.error("❌ Movie not found. Please check the name and try again.")
        else:
            st.error("⚠️ Error fetching data from the OMDB API. Try again later.")
    else:
        st.warning("🔎 Please enter a movie name to search.")

