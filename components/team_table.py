import streamlit as st
from utils.database import get_engineers_by_department

def render_team_table(df, initial, departments, editable_col, attendance_data):
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
            st.date_input("", key="mtg1", disabled=editable_col != 1)

        with col2:
            st.date_input("", key="mtg2", disabled=editable_col != 2)

        with col3:
            st.date_input("", key="mtg3",  disabled=editable_col != 3)

        with col4:
            st.date_input("", key="mtg4",  disabled=editable_col != 4)

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
                checked = attendance_data.get(dept, {}).get("m1", False)
                st.checkbox("", value=checked, key=f"{dept}_m1", disabled=editable_col != 1)

            with col2:
                checked = attendance_data.get(dept, {}).get("m2", False)
                st.checkbox("", value=checked, key=f"{dept}_m2", disabled=editable_col != 2)

            with col3:
                checked = attendance_data.get(dept, {}).get("m3", False)
                st.checkbox("", value=checked, key=f"{dept}_m3", disabled=editable_col != 3)

            with col4:
                checked = attendance_data.get(dept, {}).get("m4", False)
                st.checkbox("", value=checked,  key=f"{dept}_m4", disabled=editable_col != 4)

            attendance_data = {

            "Product Engineer": {
                "m1": True,
                "m2": False,
                "m3": False,
                "m4": False
            },
            
            "Process Engineer (SMT)": {
                "m1": True,
                "m2": True,
                "m3": False,
                "m4": False
            }
            
            }










