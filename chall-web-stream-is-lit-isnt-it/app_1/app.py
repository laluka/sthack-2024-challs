import streamlit as st
from streamlit_extras.colored_header import colored_header

colored_header(
        label="No way they find our secrets, right?",
        description="Nah. They're way too far, burried within thousands of commits hahahaha.",
        color_name="violet-70",
    )

st.image("./pic.jpg", caption="*Us knowing you won't solve this one! ;)*")

uri = st.text_input("As every good cartoon has its own plot, here's ours. We accept URIs!", "https://ipinfo.io/json")
if not uri:
    st.write("No URI. No bounty. Hah!")
    st.stop()

st.write(f"Content for uri {uri}")
import requests
rep = requests.get(uri)
st.text(rep.text)
