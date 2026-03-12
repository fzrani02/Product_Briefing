import streamlit as st
from datetime import date

def render_team_table(df, initial, departments, editable_col):

    attendance = []

    for dept in departments:

        engineers = df[(df["Initial"] == initial) & (df["Department"] == dept)]

        names = [""] + engineers["ER"].tolist()

        col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([3,3,1,3,1,1,1,1])

        with col1:
            st.write(dept)

        with col2:
            name = st.selectbox(
                "Engineer",
                names,
                key=dept+"_name",
                label_visibility="collapsed"
            )

        email=""

        if name:
            email = engineers[engineers["ER"] == name]["Email"].iloc[0]

        with col3:
            st.text_input("Ext", key=dept+"_ext", label_visibility="collapsed")

        with col4:
            st.text_input(
                "Email",
                value=email,
                key=dept+"_email",
                label_visibility="collapsed",
                disabled=True
            )

        mtg_values=[]

        for i,col in enumerate([col5,col6,col7,col8], start=1):

            with col:

                mtg = st.checkbox(
                    "",
                    key=f"{dept}_mtg{i}",
                    disabled = (i != editable_col)
                )

                mtg_values.append(mtg)

        attendance.append({
            "dept":dept,
            "name":name,
            "email":email,
            "mtg":mtg_values
        })

    return attendance
