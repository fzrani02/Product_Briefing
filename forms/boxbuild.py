import streamlit as st
import pandas as pd
from components.header import render_header
from components.project_form import render_project_form
from components.team_table import render_team_table
from datetime import date
from utils.database import load_database, get_engineers_by_department

def render_boxbuild():
    render_header()
    project_data = render_project_form()
    st.markdown("### Project Team Members")
    render_team_table()

    df = load_database()

    st.title("Product Build Briefing Checklist - BoxBuild")

    pci = st.text_input("PCI FG P/N")

    initial = pci[:2].upper() if pci else ""

    departments = [
        "Product Engineer",
        "Process Engineer (SMT)"
    ]

    st.markdown("## Meeting Attendance")

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        mtg1 = st.date_input("Mtg Date 1")

    with col2:
        mtg2 = st.date_input("Mtg Date 2")

    with col3:
        mtg3 = st.date_input("Mtg Date 3")

    with col4:
        mtg4 = st.date_input("Mtg Date 4")

    st.markdown("---")
