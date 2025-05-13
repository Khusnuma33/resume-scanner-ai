from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    text = ""
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() or ""
    except Exception as e:
        text = f"Error extracting text: {e}"
    return text

