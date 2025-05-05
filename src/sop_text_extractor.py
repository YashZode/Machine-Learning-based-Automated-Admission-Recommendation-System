# --------------------------------------------
# File: sop_text_extractor.py
# Description: Extracts raw text from PDF SOP files.
#              Assumes PDFs are digital (not scanned).
#              Uses PyMuPDF (fitz) for accurate extraction.
# --------------------------------------------

import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a digital PDF file.
    Args:
        pdf_path (str): Full path to the PDF file.
    Returns:
        str: Extracted text from the PDF.
    """
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text()
        doc.close()
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
    return text.strip()
