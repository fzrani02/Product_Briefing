import streamlit as st
from components.header import render_header
from components.project_form import render_project_form
from components.team_table import render_team_table
from utils.database import load_database

def show_pcba():

    render_header()

    project = render_project_form()

    st.markdown("### PROJECT TEAM MEMBERS")

    df = load_database()

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
    "Maintenance Engineer",
    "Test Development Engineer",
    "Program Manager",
    "Account Manager",
    "Demand Planner"
    ]

    attendance = render_team_table(
        df,
        initial="",
        departments=departments,
        editable_col=1
    )
