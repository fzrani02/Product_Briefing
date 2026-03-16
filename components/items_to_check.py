import streamlit as st

def render_items_to_check(df):

    st.markdown("## ITEMS TO CHECK")
    st.write ("NOTE: All documents/package from Design/Customer must be updated for every stage of the build including Mass Production")

    col1,col2,col3,col4 = st.columns([3,2,2,4])

    col1.markdown("**Check Item**")
    col2.markdown("**PIC**")
    col3.markdown("**Target Finish**")
    col4.markdown("**Remarks**")

    st.markdown("---")

    engineer_list = [""] + df["ER"].unique().tolist()

    items = [
        "BOM",
        "Drawing",
        "Drawing Upload to SAP or SharePoint",
        "Process Control Plan"
    ]

    for item in items:

        c1,c2,c3,c4 = st.columns([3,2,2,4])

        with c1:
            st.write(item)

        with c2:
            st.multiselect(
                "",
                engineer_list,
                key=f"pic_{item}",
                label_visibility="collapsed"
            )

        with c3:
            st.text_input(
                "",
                key=f"target_{item}",
                label_visibility="collapsed"
            )

        with c4:
            st.text_input(
                "",
                key=f"remark_{item}",
                label_visibility="collapsed"
            )
