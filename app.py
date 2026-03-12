import streamlit as st
from datetime import date
from utils.database import *

df = load_database()

st.markdown("## Team Attendance")

departments = [
    "Product Engineer",
    "Process Engineer (SMT)"
]

pci = st.text_input("PCI FG P/N")

initial = pci[:2].upper() if pci else ""

for dept in departments:

    st.markdown(f"### {dept}")

    engineers = get_engineers_by_department(df, initial, dept)

    names = engineers["ER"].tolist()

    selected = st.selectbox(
        f"{dept} Engineer",
        [""] + names,
        key=dept
    )

    email = ""

    if selected:
        email = engineers[engineers["ER"] == selected]["Email"].iloc[0]

    col1,col2,col3 = st.columns(3)

    with col1:
        st.write("Engineer:", selected)

    with col2:
        st.write("Email:", email)

    with col3:
        mtg_date = st.date_input(
            "Meeting Date",
            value=date.today(),
            key=dept+"_date"
        )
