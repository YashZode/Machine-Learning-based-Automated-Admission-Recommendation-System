# src/extract_sop_from_pdf.py
# Description: Extracts text from a scanned SOP PDF, summarizes it, and flags experience indicators

import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import textwrap

from src.sop_summarizer import summarize_text

def extract_text_from_sop(pdf_path):
    """
    Extracts text from scanned SOP PDF by rendering each page as image, then applying OCR.

    Args:
        pdf_path (str): Path to the SOP PDF file
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

def summarize_sop_and_flags(pdf_path):
    raw_text = extract_text_from_sop(pdf_path)

    # Break SOP into chunks under 512 tokens (~1000 chars)
    chunks = textwrap.wrap(raw_text, 1000)
    partial_summaries = []

    for chunk in chunks:
        prompt = (
            "Summarize the following part of a Statement of Purpose in 2-3 detailed sentences. "
            "Focus on academic background, technical achievements, project work, and long-term goals:\n\n" + chunk
        )
        partial = summarize_text(prompt, short=True)
        partial_summaries.append(partial.strip())

    final_summary_prompt = (
        "Combine the following partial summaries into a professional 8-10 sentence abstract that comprehensively captures the student's background, skills, industry exposure, research or project experience, and their specific interest in the department and university mentioned. Use an academic tone:\n\n"
        + "\n".join(partial_summaries)
    )

    final_summary = summarize_text(final_summary_prompt, short=True)

    # Extract flags from the raw text
    lower_text = raw_text.lower()
    flags = {
        'research': int("research" in lower_text or "paper" in lower_text or "publication" in lower_text),
        'professional_exp': int("professional experience" in lower_text or "worked as" in lower_text or "software engineer" in lower_text),
        'internship_exp': int("internship" in lower_text or "interned at" in lower_text or "summer intern" in lower_text)
    }

    return final_summary.strip(), flags