# --------------------------------------------
# File: sop_sentiment.py
# Description: Performs sentiment analysis on SOP text using pretrained BERT model.
#              Uses Hugging Face pipeline with SST-2 fine-tuned model.
# --------------------------------------------

from transformers import pipeline

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def get_sentiment(text):
    """
    Analyzes the sentiment of the SOP text.
    Args:
        text (str): Full SOP text.
    Returns:
        tuple: (sentiment label, confidence score)
    """
    try:
        result = sentiment_pipeline(text[:512])[0]  # truncate to 512 tokens
        return result['label'], result['score']
    except Exception as e:
        print(f"Sentiment analysis error: {e}")
        return "Neutral", 0.0
