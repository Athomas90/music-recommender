import streamlit as st
from music_recommender import get_recommendations

# Set Streamlit page configuration
st.set_page_config(page_title="Music Recommender", page_icon="🎧", layout="centered")

# Custom background CSS with no visible white block at the top
st.markdown(
    """
    <style>
    body {
        background-image: url('https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?auto=format&fit=crop&w=1740&q=80');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stApp {
        background-color: rgba(0,0,0,0);
    }
    .main-container {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        margin-top: 4rem;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.25);
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
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




