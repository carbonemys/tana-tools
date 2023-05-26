import requests
from PyPDF2 import PdfReader
from io import BytesIO

def pdf_transcript(pdf_url):
    try:
        response = requests.get(pdf_url)
        file_object = BytesIO(response.content)
        reader = PdfReader(file_object)
        text = ""

        for page in reader.pages:
            text += page.extract_text()

        return text

    except Exception as e:
        # Handle the exception gracefully
        print("An error occurred during PDF extraction:", str(e))
        return None