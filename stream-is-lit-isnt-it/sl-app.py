# https://cheat-sheet.streamlit.app/
# https://extras.streamlit.app/
# https://arnaudmiribel.github.io/streamlit-extras/extras/
# https://docs.streamlit.io/library/api-reference
# https://streamlit.io/gallery
# pip install streamlit streamlit-extras
import streamlit as st
import pandas as pd
from streamlit_extras.let_it_rain import rain
from streamlit_extras.jupyterlite import jupyterlite
from streamlit_extras.mandatory_date_range import date_range_picker
from streamlit_extras.colored_header import colored_header

colored_header(
        label="My New Pretty Colored Header",
        description="This is a description",
        color_name="violet-70",
    )

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

st.write(
        """
        This is an example of a date range picker that *always* returns a start and
        end date, even if the user has only selected one of the dates. Until the
        user selects both dates, the app will not run.
        """
    )

result = date_range_picker("Select a date range")
st.write("Result:", result)

st.slider('Pick a number', 0, 100, disabled=True)
