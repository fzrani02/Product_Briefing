import streamlit as st
import pandas as pd
from components.header import render_header
from components.project_form import render_project_form

from components.team_table import render_team_table
from components.items_to_check import render_items_to_check
from utils.revision_logic import get_editable_column
from utils.pdf_import import read_pdf, parse_form
from utils.pdf_export import generate_pdf

from datetime import date
from utils.database import load_database
from utils.autosave import autosave


def render_boxbuild():
    render_header()
        
    uploaded_pdf = st.file_uploader(
        "Upload Previous Briefing PDF",
        type=["pdf"]
    )
    
    st.markdown("---")

    project_data = render_project_form()

    
    st.markdown("---")
    df = load_database()
    pci = project_data.get("pci","")
    initial = project_data["initial"]
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

    pcis_departments = [
        "Test Development Engineer",
        "Program Manager",
        "Account Manager",
        "Demand Planner"
    ]

    editable_col =1

    revision = None
    attendance_data = {}

    if uploaded_pdf:
        revision = None   # nanti dari parser PDF
        text = read_pdf(uploaded_pdf)
    
        parsed = parse_form(text)
    
        revision = parsed["revision"]
    
        attendance_data = parsed["attendance"]
        editable_col = get_editable_column(revision, uploaded_pdf)
    
    if revision is None and uploaded_pdf is None:
        editable_col = 1
    
    elif revision is None and uploaded_pdf:
        editable_col = 2
    
    elif revision == "A":
        editable_col = 3
    
    elif revision == "B":
        editable_col = 4

   
    
    render_team_table(
        df,
        initial,
        departments,
        editable_col,
        attendance_data,
        "PROJECT TEAM MEMBERS (PLANTS)",
        "plant"
    )
    
    
    st.markdown("---")

    render_team_table(
        df,
        initial,
        pcis_departments,
        editable_col,
        attendance_data,
        "PROJECT TEAM MEMBERS (PCIS)",
        "pcis"
    )
    autosave()

    st.markdown("---")
    render_items_to_check(df)
    st.markdown("---")

    if st.button("Export to PDF"):
    
        pdf_file = (project_data, departments, pcis_department)

        st.download_button(
            label="Download PDF",
            data=pdf_file,
            
            file_name="product_briefing.pdf",
            mime="application/pdf"
        )
    
