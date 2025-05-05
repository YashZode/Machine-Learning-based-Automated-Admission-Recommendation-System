# --------------------------------------------
# File: sop_classifier.py
# Description: Uses a zero-shot classification model to evaluate if a student
#              is a Strong, Average, or Weak candidate based on SOP content.
#              Powered by Hugging Face transformers (BART MNLI).
# --------------------------------------------

from transformers import pipeline

# Load zero-shot classifier
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_sop(text):
    """
    Uses a zero-shot classifier to assess candidate strength based on SOP.
    Args:
        text (str): SOP text.
    Returns:
        tuple: (classification label, model explanation string)
    """
    try:
        labels = ["Strong candidate", "Average candidate", "Weak candidate"]
        hypothesis_template = "This SOP indicates the student is a {}."

        result = classifier(text[:1024], labels, hypothesis_template=hypothesis_template)
        best_label = result['labels'][0]
        confidence = result['scores'][0]

        # Use stricter threshold logic
        if confidence > 0.75:
            final_label = best_label
        elif confidence > 0.50:
            final_label = "Average candidate"
        else:
            final_label = "Weak candidate"

        return final_label.replace(" candidate", ""), f"{final_label} ({confidence:.2f})"
    except Exception as e:
        print(f"Classification error: {e}")
        return "Unknown", "[Classification failed]"
