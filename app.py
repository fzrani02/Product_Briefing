import streamlit as st
from datetime import date
from utils.database import load_database, get_customer_by_initial

st.set_page_config(layout="wide")

# Load database
df = load_database()

# HEADER
col1, col2 = st.columns([1,4])

with col1:
    st.image("logo.png", width=120)

with col2:
    st.markdown(
        "<h1 style='text-align:center;'>PRODUCT BUILD BRIEFING CHECKLIST</h1>",
        unsafe_allow_html=True
    )

st.markdown("---")

# FORM
c1, c2, c3 = st.columns(3)

with c1:
    project_name = st.text_input("Project Name")
    build_type = st.text_input("Build Type")
    date_updated = st.date_input("Date Updated", value=date.today())

with c2:
    pci = st.text_input("PCI FG P/N")

    initial = pci[:2].upper() if pci else ""

    customer = get_customer_by_initial(df, initial)

    st.text_input("Customer", value=customer, disabled=True)

    project_account = st.text_input("Project Account")

with c3:
    revision = st.text_input("Revision", value="00", disabled=True)

    product_type = st.selectbox(
        "Product Type",
        ["Automotive", "Medical", "Military", "Consumer"]
    )

st.markdown("---")

st.write("Next step: Team members table")
