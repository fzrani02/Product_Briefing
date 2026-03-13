import streamlit as st
from utils.database import get_engineers_by_department


def render_team_table(df, initial, departments, editable_col):

    st.markdown("### PROJECT TEAM MEMBERS (PLANT)")

    # header tabel
    st.markdown("""
    <table style="width:100%; border-collapse: collapse; text-align:center;">
    <tr>
        <th rowspan="2" style="border:1px solid black;">Department</th>
        <th rowspan="2" style="border:1px solid black;">Name</th>
        <th rowspan="2" style="border:1px solid black;">Ext. #</th>
        <th rowspan="2" style="border:1px solid black;">Email</th>
        <th colspan="4" style="border:1px solid black;">Attendances</th>
    </tr>
    <tr>
        <th style="border:1px solid black;">Mtg</th>
        <th style="border:1px solid black;">Mtg</th>
        <th style="border:1px solid black;">Mtg</th>
        <th style="border:1px solid black;">Mtg</th>
    </tr>
    </table>
    """, unsafe_allow_html=True)

    attendance = []

    for dept in departments:

        engineers = get_engineers_by_department(df, initial, dept)

        engineer_list = [""] + engineers["ER"].tolist()

        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

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
