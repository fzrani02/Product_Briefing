import streamlit as st
from datetime import date 

def render_project_form():
  col1, col2, col3 = st.columns(3)
  
  with col1:
    project_name = st.text_input("Project Name")
    build_type = st.text_input("Build Type")
    date_updated = st.date_input("Date Updated", value=date.today())

  with col2:
    pci = st.text_input("PCI FG P/N")
    customer = st.text_input("Customer", disabled=True)
    project_account = st.text_input("Project Account")

  with col3:
    revision = st.text_input("Revision", disabled=True)
    product_type = st.selectbox(
      "Product Type",
      ["Automotive","Medical","Military","Consumer"]
    )
  
  return {
    "project_name": project_name,
    "build_type": build_type,
    "data_updated": date_updated, 
    "pci": pci,
    "customer": customer,
    "project_account": project_account,
    "revision": revision,
    "product_type": product_type
  }
  
