# 🎓 AI-Powered Admission Recommendation System

This project is an end-to-end **Machine Learning-based Admission Recommendation System** designed to automate graduate application evaluation. It ingests scanned **Statements of Purpose (SOPs)** and **Letters of Recommendation (LORs)**, extracts meaningful features using NLP, and predicts admission probability based on academic and qualitative inputs.

## 🚀 Features

- 🧠 **OCR & NLP Pipeline**: Extracts and summarizes scanned PDFs using PyMuPDF, Tesseract OCR, and Transformer-based summarization (LaMini-Flan-T5).
- 🔍 **Text Scoring**: Quantifies SOPs and LORs based on keyword density, technical strengths, research, and endorsement quality.
- 📈 **Admission Prediction**: Predicts chance of admission using a trained **Linear Regression model**.
- 🌐 **Web Interface**: Flask-based frontend for uploading PDFs and displaying prediction results.
- 📊 **Dashboard Output**: Shows predicted probability, classification (High/Medium/Low), and summaries.

## 🛠 How It Works

1. **Upload PDFs**: Users upload SOP and LOR PDFs on the UI.
2. **Score Input Fields**: Enter TOEFL, GPA, and optional GRE score.
3. **Processing**:
   - SOP/LORs are parsed → OCR processed → summarized.
   - Scores and flags are extracted and converted to numerical features.
   - Model infers the chance of admission.
4. **View Results**: Outputs include:
   - Admission Chance (e.g., 78.78%)
   - Summary of SOP & LOR
   - Classification: High, Medium, Low

### Install dependencies
pip install -r requirements.txt

### Run the app
python app.py

### Visit in browser
Open http://127.0.0.1:5000

### Project Structure
src/
├── extract_sop_from_pdf.py
├── sop_summarizer.py
├── sop_classifier.py
├── score_sop_lor.py
├── train_admit_model.py
├── predict_admission.py
├── ...
static/
templates/
uploads/
app.py
requirements.txt


📌 Notes
Ensure uploaded PDFs are scanned clearly for accurate OCR.

This system is intended to assist in admission decisions, not replace human review.

🤝 Acknowledgment
Developed as a Capstone Project at the University of Wisconsin-Milwaukee.
Advised by Dr. Prasenjit Guptasarma, Department of Computer Science.
