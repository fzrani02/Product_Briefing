from reportlab.pdfgen import canvas

def generate_pdf(project_name):

    c = canvas.Canvas("report.pdf")

    c.drawString(100,750,f"Project : {project_name}")

    c.save()
