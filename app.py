import streamlit as st
from music_recommender import get_recommendations

# Set page config for title and icon
st.set_page_config(page_title="Music Recommender", page_icon="🎧", layout="centered")

# Add background style using custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: #f2f2f2;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .main {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='main'>", unsafe_allow_html=True)

st.title("🎵 Music Recommender")
st.write("Get music recommendations based on the style of your favorite artists.")

# User input
artist = st.text_input("🎤 Enter an artist name:")

if artist:
    recs = get_recommendations(artist)
    st.subheader("🎧 Recommended Tracks:")
    for rec in recs:
        st.markdown(f"- {rec}")

st.markdown("</div>", unsafe_allow_html=True)
