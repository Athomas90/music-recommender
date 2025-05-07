import streamlit as st
from music_recommender import get_recommendations

st.title("🎵 Music Recommender")
st.write("Enter an artist to get stylistically similar songs!")

artist = st.text_input("Enter artist name:")

if artist:
    recs = get_recommendations(artist)
    st.subheader("Recommendations:")
    for rec in recs:
        st.write("- " + rec)
