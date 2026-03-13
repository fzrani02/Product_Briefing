import streamlit as st
from utils.database import get_engineers_by_department

def render_team_table(df, initial, departments, editable_col):
    st.markdown("""
    <style>
    div[data-testid="stCheckbox"] {
        display:flex;
        justify-content:center;
    }
    </style>
    """, unsafe_allow_html=True)

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
            st.date_input("", key="mtg1")

        with col2:
            st.date_input("", key="mtg2", disabled=True)

        with col3:
            st.date_input("", key="mtg3",  disabled=True)

        with col4:
            st.date_input("", key="mtg4",  disabled=True)

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
                    "",
                    engineer_list,
                    key=f"{dept}_engineer"
                )

            email = ""
            if selected:
                email = engineers[engineers["ER"] == selected]["Email"].iloc[0]

            with col3:
                st.text_input("", key=f"{dept}_ext")

            with col4:
                st.text_input(
                    "",
                    value=email,
                    disabled=True,
                    key=f"{dept}_email"
                )

        with right:

            col1,col2,col3,col4 = st.columns(4)

            with col1:
                st.checkbox("",key=f"{dept}_m1")

            with col2:
                st.checkbox("", key=f"{dept}_m2")

            with col3:
                st.checkbox("", key=f"{dept}_m3")

            with col4:
                st.checkbox("", key=f"{dept}_m4")








