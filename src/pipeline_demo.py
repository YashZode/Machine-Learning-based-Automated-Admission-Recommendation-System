#!/usr/bin/env python
import os, sys

# make sure Python can see your src/ folder
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from extract_sop_from_pdf import summarize_sop_and_flags
from extract_lor_from_pdf import summarize_lor_and_flags
from score_sop_lor      import score_sop, score_lor
from sop_classifier     import classify_sop
from sop_quality        import assess_quality
from sop_sentiment      import get_sentiment
# from predict_admission import predict_admission_chance
from predict_admission import predict_admission_chance

def main():
    # 1) Paths to your sample PDFs (adjust these)
    sop_pdf = "E:/Spring_2025/CapstoneProject/13th April 2025______Final/ShowTime(YASH)/sample_data/1.pdf"
    lor_pdf = "E:/Spring_2025/CapstoneProject/13th April 2025______Final/ShowTime(YASH)/sample_data/yash_lor.pdf"

    # 2) Extract & summarize
    sop_summary, sop_flags = summarize_sop_and_flags(sop_pdf)
    lor_summary, lor_flags = summarize_lor_and_flags(lor_pdf)

    # 3) Score & classify
    sop_keyword_score = score_sop(sop_summary)
    lor_keyword_score = score_lor(lor_summary)
    sop_label, sop_explanation = classify_sop(sop_summary)
    sop_quality_score = assess_quality(sop_summary)
    sentiment_label, sentiment_conf  = get_sentiment(sop_summary)

    # 4) Predict admission
    # substitute your actual numeric values here or hook up to your data sources
    features = {
        "gre_score":          325,
        "toefl_score":        115,
        "university_rating":  4,
        "sop_score":          sop_keyword_score,
        "lor_score":          lor_keyword_score,
        "gpa":                9.1,
        "research":           int(sop_flags["research"] or lor_flags["research"]),
        # "professional_exp":   lor_flags["professional_exp"],
        # "internship_exp":     sop_flags["internship_exp"],
    }
    

    admit = predict_admission_chance(
    features['gre_score'],
    features['toefl_score'],
    features['university_rating'],
    features['sop_score'],
    features['lor_score'],
    features['gpa'],
    features['research']
    )



    # 5) Print everything out
    print("\n📝 SOP Summary:\n", sop_summary)
    print("🚩 SOP Flags:",        sop_flags)
    print("✅ SOP Keyword Score:", sop_keyword_score)
    print("🔍 SOP Classification:", sop_label, sop_explanation)
    print("✍️  SOP Quality Score:", sop_quality_score)
    print("😊 SOP Sentiment:",     sentiment_label, f"({sentiment_conf:.2f})")

    print("\n📝 LOR Summary:\n", lor_summary)
    print("🚩 LOR Flags:",        lor_flags)
    print("✅ LOR Keyword Score:", lor_keyword_score)

    print("\n🎓 Admission Prediction:")
    print(f"   Chance of Admit: {admit['admit_chance']}%")
    print(f"   Classification:  {admit['classification']}")

if __name__ == "__main__":
    main()
