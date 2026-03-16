from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import streamlit as st
import io


def generate_pdf():

    buffer = io.BytesIO()

    c = canvas.Canvas(buffer, pagesize=A4)

    y = 800

    c.setFont("Helvetica", 10)

    for key, value in st.session_state.items():

        text = f"{key} : {value}"

        c.drawString(50, y, text)

        y -= 15

        if y < 50:
            c.showPage()
            y = 800

    c.save()

    buffer.seek(0)

    return buffer
