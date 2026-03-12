import streamlit as st
from datetime import date
from utils.database import get_engineers_by_department
from st_aggrid import AgGrid
import pandas as pd
from forms.boxbuild import render_boxbuild
from forms.pcba import render_pcba

st.set_page_config(layout="wide")

st.sidebar.title("Form Selection")

form_type = st.sidebar.radio(
    "Choose Form",
    ["BoxBuild", "PCBA"]
)

if form_type == "BoxBuild":
    render_boxbuild()

elif form_type == "PCBA":
    render_pcba()

uploaded_pdf = st.file_uploader(
    "Import Existing Briefing Form",
    type=["pdf"]
)

if uploaded_pdf:

    text = read_pdf(uploaded_pdf)

    parsed = parse_form(text)

    project = parsed["project"]

    st.text_input("Project Name", value=project)
    
df = load_database()

st.title("Team Attendance")

departments = [
"Product Engineer",
"Process Engineer (SMT)",
"Department 3",
"Department 4",
"Department 5",
"Department 6",
"Department 7",
"Department 8",
"Department 9",
"Department 10",
"Department 11",
"Department 12",
"Department 13",
"Department 14",
"Department 15",
"Department 16",
"Department 17",
"Department 18",
"Department 19"
]

pci = st.text_input("PCI FG P/N")

if initial:
    table_rows = []
    for dept in departements:
        engineer = get_engineers_by_department(df,initial,dept)
        engineer_list = engineer["ER"].tolist()
        table_rows.append({
            "Department": dept,
            "Name":"",
            "Ext":"",
            "Email":"",
            "Mtg Date 1": "",
            "Mtg Date 2": "",
            "Mtg Date 3": "",
            "Mtg Date 4": "",
            "Engineer Options": engineer_list
        })
    attendance_df = pd.DataFrame(table_rows)
    st.markdown("## Team Attendance")

    grid_response = AgGrid(
        attendance_df,
        editable=True,
        height=500
    )
    
    attendance_result = grid_response["data"]

initial = pci[:2].upper() if pci else ""

st.markdown("---")

for dept in departments:
    engineers = get_engineers_by_department(df, initial, dept)
    engineer_list = [""] + engineers["ER"].tolist()

    col1, col2, col3, col4 = st.columns([3,3,2,3])

    with col1:
        st.write(dept)

    with col2:
        selected = st.selectbox(
            "Engineer",
            engineer_list,
            key=f"{dept}_engineer"
        )

    email = ""

    if selected:
        email = engineers[engineers["ER"] == selected]["Email"].iloc[0]

    with col3:
        st.text_input(
            "Email",
            value=email,
            disabled=True,
            key=f"{dept}_email"
        )

    st.date_input(
        "Meeting Date",
        value=date.today(),
        key=f"{dept}_date"
    )

for dept in departments:

    engineers = get_engineers_by_department(df, initial, dept)

    engineer_list = [""] + engineers["ER"].tolist()

    col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)

    with col1:
        st.write(dept)

    with col2:
        selected = st.selectbox(
            "ER",
            engineer_list,
            key=f"{dept}_er"
        )

    email = ""

    if selected:
        email = engineers[engineers["ER"] == selected]["Email"].iloc[0]

    with col3:
        st.text_input(
            "Email",
            value=email,
            disabled=True,
            key=f"{dept}_email"
        )

    with col4:
        st.text_input("Ext", key=f"{dept}_ext")

    with col5:
        st.checkbox("", key=f"{dept}_m1")

    with col6:
        st.checkbox("", key=f"{dept}_m2")

    with col7:
        st.checkbox("", key=f"{dept}_m3")

    with col8:
        st.checkbox("", key=f"{dept}_m4")







