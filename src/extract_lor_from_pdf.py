# --------------------------------------------
# File: extract_lor_from_pdf.py
# Description: Extracts text from a scanned LOR PDF, summarizes it, and flags experience indicators
# --------------------------------------------

import pytesseract
from PIL import Image
import fitz  # PyMuPDF
from src.sop_summarizer import summarize_text


def extract_text_from_lor(pdf_path):
    """
    Extracts text from scanned LOR PDF by rendering each page as image, then applying OCR.

    Args:
        pdf_path (str): Path to the LOR PDF file
    Returns:
        str: Extracted plain text
    """
    text = ""
    doc = fitz.open(pdf_path)

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap(dpi=300)
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        text += pytesseract.image_to_string(image) + "\n"

    return text.strip()


def summarize_lor_and_flags(pdf_path):
    raw_text = extract_text_from_lor(pdf_path)

    prompt = (
        "Summarize this Letter of Recommendation in 4-6 professional sentences. "
        "Include the recommender's tone, evaluation of the student's academic or professional strengths, "
        "and conclude whether the student is highly recommended:\n\n" + raw_text
    )
    summary = summarize_text(prompt, short=False)

    # Extract flags from the raw text
    lower_text = raw_text.lower()
    flags = {
        'research': int(any(k in lower_text for k in ["research", "publication", "paper"])),
        # include broader experience keywords
        'professional_exp': int(any(k in lower_text for k in [
            "professional experience", "worked as", "employment", "job", "experience"
        ])),
        'internship_exp': int(any(k in lower_text for k in ["internship", "intern"]))
    }

    return summary.strip(), flags
