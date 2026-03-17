from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.platypus import Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import streamlit as st
import io


def generate_pdf(project_data, departments, pcis_departments):

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )

    styles = getSampleStyleSheet()
    elements = []

    logo = Image("logo.png", width=120, height=40)

    title = Paragraph(
        "<para align=center><b>PRODUCT BUILD BRIEFING CHECKLIST</b></para>",
        styles['Title']
    )
    
    np_info = Paragraph(
        "<para align=right>NP-F-006<br/>20 Feb 2026</para>",
        styles['Normal']
    )
    
    header_table = Table(
        [[logo, title, np_info]],
        colWidths=[120, 320, 120]
    )
    
    header_table.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
    ]))
    
    elements.append(header_table)
    elements.append(Spacer(1,20))

    # =========================
    # TITLE
    # =========================

    
    # =========================
    # PROJECT INFO
    # =========================

    project_table = [
        ["Project Name", project_data["project_name"], "Customer", project_data["customer"]],
        ["Build Type", project_data["build_type"], "PCI FG P/N", project_data["pci"]],
        ["Project Account", project_data["project_account"], "Product Type", project_data["product_type"]],
        ["Date Updated", str(project_data["date_updated"]), "Revision", project_data["revision"]],
    ]

    t = Table(project_table, colWidths=[120,160,120,120])

    t.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,0),(0,-1),colors.lightgrey),
        ("BACKGROUND",(2,0),(2,-1),colors.lightgrey),
    ]))

    elements.append(t)
    elements.append(Spacer(1,25))

    # =========================
    # TEAM MEMBERS
    # =========================

    elements.append(Paragraph("<b>PROJECT TEAM MEMBERS (PLANT)</b>", styles['Heading3']))
    elements.append(Spacer(1,10))

    team_data = [["Department","Name","Ext","Email","M1","M2","M3","M4"]]

    for dept in departments:

        team_data.append([
            dept,
            st.session_state.get(f"{dept}_engineer",""),
            st.session_state.get(f"{dept}_ext",""),
            st.session_state.get(f"{dept}_email",""),
            "✓" if st.session_state.get(f"{dept}_m1") else "",
            "✓" if st.session_state.get(f"{dept}_m2") else "",
            "✓" if st.session_state.get(f"{dept}_m3") else "",
            "✓" if st.session_state.get(f"{dept}_m4") else "",
        ])

    team_table = Table(team_data, hAlign='LEFT')

    team_table.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
        ("ALIGN",(4,1),(-1,-1),"CENTER")
    ]))

    elements.append(team_table)
    elements.append(Spacer(1,25))

    # =========================
    # PCIS TEAM
    # =========================

    elements.append(Paragraph("<b>PROJECT TEAM MEMBERS (PCIS)</b>", styles['Heading3']))
    elements.append(Spacer(1,10))

    pcis_data = [["Department","Name","Ext","Email","M1","M2","M3","M4"]]

    for dept in pcis_departments:

        pcis_data.append([
            dept,
            st.session_state.get(f"{dept}_engineer",""),
            st.session_state.get(f"{dept}_ext",""),
            st.session_state.get(f"{dept}_email",""),
            "✓" if st.session_state.get(f"{dept}_m1") else "",
            "✓" if st.session_state.get(f"{dept}_m2") else "",
            "✓" if st.session_state.get(f"{dept}_m3") else "",
            "✓" if st.session_state.get(f"{dept}_m4") else "",
        ])

    pcis_table = Table(pcis_data, hAlign='LEFT')

    pcis_table.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
        ("ALIGN",(4,1),(-1,-1),"CENTER")
    ]))

    elements.append(pcis_table)
    elements.append(Spacer(1,25))

    # =========================
    # ITEMS TO CHECK
    # =========================

    elements.append(Paragraph("<b>ITEMS TO CHECK</b>", styles['Heading3']))
    elements.append(Spacer(1,10))

    item_table = [["Item","PIC","Target","Remark"]]

    for key in st.session_state:

        if key.startswith("remark_"):

            item = key.replace("remark_","")
            pic = ", ".join(st.session_state.get(f"pic_{item}",[]))
            target = st.session_state.get(f"target_{item}","")
            remark = st.session_state.get(key,"")

            item_table.append([item,pic,target,remark])

    items = Table(item_table, hAlign='LEFT')

    items.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey)
    ]))

    elements.append(items)

    doc.build(elements)

    buffer.seek(0)

    return buffer
