import streamlit as st

audio_url = 'https://stream.nightride.fm/chillsynth.mp3'

st.set_page_config(page_title="radio chill", page_icon="🎵", layout="centered")
st.title("Radio Chill")
st.markdown("**Clique no botão abaixo para iniciar a reprodução do áudio.**")

audio_html = f"""
<audio controls autoplay>
    <source src="{audio_url}" type="audio/mpeg">
    Seu navegador não suporta o elemento de áudio.
</audio>
"""
st.markdown(audio_html, unsafe_allow_html=True)