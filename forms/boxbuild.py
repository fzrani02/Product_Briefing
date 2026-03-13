import streamlit as st
import pandas as pd
from components.header import render_header
from components.project_form import render_project_form

from components.team_table import render_team_table

from datetime import date
from utils.database import load_database

def render_boxbuild():
    render_header()
    
    project_data = render_project_form()
    st.markdown("---")
    df = load_database()
    pci = project_data.get("pci","")
    initial = pci[:2].upper() if pci else ""
    departments = [
        "Product Engineer",
        "Process Engineer (SMT)",
        "Process Engineer (Back End)",
        "Test Engineer (FCT)",
        "Test Engineer (ICT)",
        "Production Supervisor (SMT)",
        "Production Supervisor (Back End)",
        "QA Engineer",
        "QC Engineer (IPQC)",
        "QC Engineer (OQC)",
        "QC Engineer (IQC)",
        "Material Controller",
        "COB Engineer",
        "DFM Engineer",
        "Maintenance Engineer"
    ]

    editable_col =1

    revision = None
    uploaded_pdf = st.file_uploader("Upload Previous PDF", type=["pdf"])
    
    if uploaded_pdf:
        revision = None   # nanti dari parser PDF
    
    if revision is None and uploaded_pdf is None:
        editable_col = 1
    
    elif revision is None and uploaded_pdf:
        editable_col = 2
    
    elif revision == "A":
        editable_col = 3
    
    elif revision == "B":
        editable_col = 4
    render_team_table(df, initial, departments, editable_col)

