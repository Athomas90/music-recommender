import streamlit as st
from music_recommender import get_recommendations

# Set basic Streamlit page config
st.set_page_config(page_title="Music Recommender", page_icon="🎧", layout="centered")

# Minimal styling for a clean white theme
st.markdown(
    """
    <style>
    body {
        background-color: white;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stApp {
        background-color: white;
    }
    .main-container {
        background-color: white;
        padding: 2rem;
        max-width: 700px;
        margin: 4rem auto;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='main-container'>", unsafe_allow_html=True)

st.title("🎵 Music Recommender")
st.write("Get music recommendations based on the style of your favorite artists.")

artist = st.text_input("🎤 Enter an artist name:")

if artist:
    recs = get_recommendations(artist)
    st.subheader("💡 Recommended Tracks:")
    for rec in recs:
        st.markdown(f"- {rec}")

st.markdown("</div>", unsafe_allow_html=True)

