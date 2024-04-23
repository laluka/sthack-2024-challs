import streamlit as st
from streamlit_extras.colored_header import colored_header

colored_header(
        label="Oh nom nom nom I love eating URIs!",
        description="I sure do! :)",
        color_name="violet-70",
    )

st.image('./nomnomnom-cat.jpg', caption='Cat eating a single URI')

uri = st.text_input('Feed me URI!', "https://ipinfo.io/json")
if not uri:
    st.write("No URI set, I'm hungry pal.")
    st.stop()

st.write(f"Content for uri {uri}")
import requests
rep = requests.get(uri)
st.text(rep.text)
