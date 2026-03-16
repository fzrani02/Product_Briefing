import json
import streamlit as st 

def autosave():
  data= dict(st.session_state)
  with open("autosave.json", "w") as f:
    json.dump(data, f)
