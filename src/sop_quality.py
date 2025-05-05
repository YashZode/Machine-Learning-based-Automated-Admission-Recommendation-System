# --------------------------------------------
# File: sop_quality.py
# Description: Calculates a basic quality score for an SOP based on readability,
#              grammar, and length. This is a proxy for assessing overall structure and coherence.
# --------------------------------------------

import textstat

# Install with: pip install textstat

def assess_quality(text):
    """
    Assesses the quality of an SOP based on various linguistic metrics.
    Args:
        text (str): SOP text.
    Returns:
        int: Quality score between 0 and 100.
    """
    try:
        flesch = textstat.flesch_reading_ease(text)         # Higher = easier to read
        grammar_penalty = text.count('..') * 5              # Penalize bad punctuation
        length_score = min(len(text.split()) / 10, 100)     # Encourage detailed writing

        score = flesch + length_score - grammar_penalty
        return int(max(0, min(score, 100)))
    except Exception as e:
        print(f"Quality scoring error: {e}")
        return 50
