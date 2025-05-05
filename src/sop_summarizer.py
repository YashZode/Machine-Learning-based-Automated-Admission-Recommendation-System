# src/sop_summarizer.py
# Description: Summarizes SOP text and infers experience flags

import torch
from transformers import pipeline
import textwrap

summarizer = pipeline("text2text-generation", model="MBZUAI/LaMini-Flan-T5-248M", device=0 if torch.cuda.is_available() else -1)

def summarize_text(text, short=False):
    if short:
        text = text[:1500]
        prompt = (
            "Summarize this Statement of Purpose in 5 professional sentences. "
            "Include the student's academic background, technical strengths, projects , internships, industry experience, and career goals. Also mention the University name if provided:\n\n"
            + text
        )
        result = summarizer(prompt, max_length=220, min_length=100, do_sample=False)[0]['generated_text']
        return result.strip()
    else:
        chunks = textwrap.wrap(text, 1024)
        results = []
        for chunk in chunks:
            res = summarizer("Summarize this:\n" + chunk, max_length=120, min_length=40, do_sample=False)[0]['generated_text']
            results.append(res)
        return " ".join(results)

def infer_experience_flags(text):
    text = text.lower()
    return {
        "research": any(k in text for k in ["research", "publication", "paper"]),
        "experience": any(k in text for k in ["full-time", "professional experience", "worked at", "employment"]),
        "internship": any(k in text for k in ["internship", "interned", "summer intern"])
    }