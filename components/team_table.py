import streamlit as st
from utils.database import get_engineers_by_department

def render_team_table(df, initial, departments, editable_col, attendance_data):

    # CSS
    st.markdown("""
    <style>

    div[data-testid="stCheckbox"] {
        display:flex;
        justify-content:center;
        align-items: center;
        width: 100%;
        padding-top: 5 px;
    }
    
    div[data-testid="stCheckbox"] > label {
        width: fit-content !important;
        margin: 0 auto !important;
    }

    div[data-testid="stTextInput"], div[data-testid="stSelectbox"] {
        margin-top:-15px;
    }

    .column-text{
        padding-top: 10px;
        font-size: 14px;
    }

    </style>
    """, unsafe_allow_html=True)

    # HEADER
    left, right = st.columns([3,2])

    with left:
        st.markdown("### PROJECT TEAM MEMBERS (PLANTS)")

        col1,col2,col3,col4 = st.columns([3,3,2,3])
        
        col1.markdown("<p style='text-align: center; font-weight: bold;'>Department</p>", unsafe_allow_html=True)
        col2.markdown("<p style='text-align: center; font-weight: bold;'>Name</p>", unsafe_allow_html=True)
        col3.markdown("<p style='text-align: center; font-weight: bold;'>Ext. #</p>", unsafe_allow_html=True)
        col4.markdown("<p style='text-align: center; font-weight: bold;'>Email</p>", unsafe_allow_html=True)

    with right:

        st.markdown("<h3 style='text-align: center;'>ATTENDANCES</h3>", unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        # Tanggal juga diposisikan (Streamlit widget secara default lebar penuh)
        with col1: st.date_input("", key="mtg1", disabled=editable_col != 1, label_visibility="collapsed")
        with col2: st.date_input("", key="mtg2", disabled=editable_col != 2, label_visibility="collapsed")
        with col3: st.date_input("", key="mtg3", disabled=editable_col != 3, label_visibility="collapsed")
        with col4: st.date_input("", key="mtg4", disabled=editable_col != 4, label_visibility="collapsed")

    st.markdown("---")

        with col1:
            st.date_input("", key="mtg1", disabled=editable_col != 1, label_visibility="collapsed")

        with col2:
            st.date_input("", key="mtg2", disabled=editable_col != 2, label_visibility="collapsed")

        with col3:
            st.date_input("", key="mtg3", disabled=editable_col != 3, label_visibility="collapsed")

        with col4:
            st.date_input("", key="mtg4", disabled=editable_col != 4, label_visibility="collapsed")

    st.markdown("---")

    # ROW DATA
    
    for dept in departments:
        # (Logika pengambilan data Anda tetap sama)
        engineers = get_engineers_by_department(df, initial, dept)
        engineer_list = [""] + engineers["ER"].tolist()

        left, right = st.columns([3,2])

        with left:
            col1, col2, col3, col4 = st.columns([3,3,2,3])
            
            with col1:
                # Tambahkan class CSS agar teks department sejajar dengan input di sampingnya
                st.markdown(f"<div class='column-text' style='text-align: center;'>{dept}</div>", unsafe_allow_html=True)

            with col2:
                selected = st.selectbox("", engineer_list, key=f"{dept}_engineer", label_visibility="collapsed")

            # ... (logika email Anda)
            email_key = f"{dept}_email"
            email = ""
            if selected:
                email = engineers.loc[engineers["ER"] == selected, "Email"].values[0]
            st.session_state[email_key] = email

            with col3:
                st.text_input("", key=f"{dept}_ext", label_visibility="collapsed")

            with col4:
                st.text_input("", key=email_key, disabled=True, label_visibility="collapsed")

        with right:
            col1, col2, col3, col4 = st.columns(4)
            # Checkbox sekarang akan otomatis ke tengah berkat CSS di atas
            for i, col in enumerate([col1, col2, col3, col4], 1):
                with col:
                    checked = attendance_data.get(dept, {}).get(f"m{i}", False)
                    st.checkbox("", value=checked, key=f"{dept}_m{i}", disabled=editable_col != i)
    

       








