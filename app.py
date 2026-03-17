import streamlit as st
from forms.boxbuild import render_boxbuild

st.set_page_config(layout="wide")

st.sidebar.title("Form Selection")

form_type = st.sidebar.radio(
    "Select Form",
    ["BoxBuil"]
)

if form_type == "BoxBuil":
    render_boxbuild()
