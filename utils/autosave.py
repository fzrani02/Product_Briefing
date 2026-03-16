import json
import streamlit as st


def autosave():

    clean_data = {}

    for key, value in st.session_state.items():

        try:
            json.dumps(value)  # cek apakah bisa diserialisasi
            clean_data[key] = value

        except TypeError:
            clean_data[key] = str(value)  # fallback jadi string

    with open("autosave.json", "w") as f:
        json.dump(clean_data, f, indent=2)
