import streamlit as st
from utils.database import get_engineers_by_department

def render_team_table(df, initial, departments, editable_col):

    # HEADER LAYOUT
    left, right = st.columns([3,2])

    with left:
        st.markdown("### PROJECT TEAM MEMBERS (PLANTS)")
        col1,col2,col3,col4 = st.columns([3,3,2,3])
        col1.markdown("**Department**")
        col2.markdown("**Name**")
        col3.markdown("**Ext. #**")
        col4.markdown("**Email**")

    with right:
        st.markdown("### ATTENDANCES")

        col1,col2,col3,col4 = st.columns(4)

        with col1:
            st.date_input("")

        with col2:
            st.date_input("Mtg Date 2")

        with col3:
            st.date_input("Mtg Date 3")

        with col4:
            st.date_input("Mtg Date 4")

    st.markdown("---")

    # ROW DATA
    for dept in departments:

        engineers = get_engineers_by_department(df, initial, dept)
        engineer_list = [""] + engineers["ER"].tolist()

        left, right = st.columns([3,2])

        with left:

            col1,col2,col3,col4 = st.columns([3,3,2,3])

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
                st.text_input("Ext", key=f"{dept}_ext")

            with col4:
                st.text_input(
                    "Email",
                    value=email,
                    disabled=True,
                    key=f"{dept}_email"
                )

        with right:

            col1,col2,col3,col4 = st.columns(4)

            with col1:
                st.checkbox("")

            with col2:
                st.checkbox("", key=f"{dept}_m2")

            with col3:
                st.checkbox("", key=f"{dept}_m3")

            with col4:
                st.checkbox("", key=f"{dept}_m4")





