import pdfplumber

def read_pdf(uploaded_file):

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    return text


def parse_form(text):

    return {
        "revision": None,
        "attendance": {}
    }
