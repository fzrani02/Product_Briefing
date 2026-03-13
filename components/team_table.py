import streamlit as st
from utils.database import get_engineers_by_department


def render_team_table(df, initial, departments, editable_col):

    # header tabel
    st.markdown("""
    <table style="width:100%; border-collapse: collapse; text-align:center;">
    <tr>
        <th rowspan="2">Department</th>
        <th rowspan="2">Name</th>
        <th rowspan="2">Ext. #</th>
        <th rowspan="2">Email</th>
        <th colspan="4">Attendances</th>
    </tr>
    <tr>
        <th>Mtg</th>
        <th>Mtg</th>
        <th>Mtg</th>
        <th>Mtg</th>
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
                key=f"{dept}_er"
            )
            
        with col3:
            st.text_input("Ext", key=f"{dept}_ext")

        email = ""

        if selected:
            email = engineers[engineers["ER"] == selected]["Email"].iloc[0]

        with col4:
            st.text_input(
                "Email",
                value=email,
                disabled=True,
                key=f"{dept}_email"
            )

        with col5:
            st.checkbox("", key=f"{dept}_m1")

        with col6:
            st.checkbox("", key=f"{dept}_m2")

        with col7:
            st.checkbox("", key=f"{dept}_m3")

        with col8:
            st.checkbox("", key=f"{dept}_m4")



