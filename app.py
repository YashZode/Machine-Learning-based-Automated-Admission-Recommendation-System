# src/app.py
# Description: Flask app to upload SOP & LOR PDFs and predict admission chances

import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from src.extract_sop_from_pdf import summarize_sop_and_flags
from src.extract_lor_from_pdf import summarize_lor_and_flags
from src.score_sop_lor import score_sop, score_lor
from src.predict_admission import predict_admission_chance

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Parse form inputs
        toefl_score = float(request.form['toefl'])
        cgpa_value = float(request.form['gpa'])
        gre_raw = request.form.get('gre')
        gre_score = float(gre_raw) if gre_raw else None

        # Save uploaded SOP and LOR files
        sop_file = request.files['sop_pdf']
        lor_file = request.files['lor_pdf']
        sop_filename = secure_filename(sop_file.filename)
        lor_filename = secure_filename(lor_file.filename)
        sop_path = os.path.join(app.config['UPLOAD_FOLDER'], sop_filename)
        lor_path = os.path.join(app.config['UPLOAD_FOLDER'], lor_filename)
        sop_file.save(sop_path)
        lor_file.save(lor_path)

        # Summarize SOP and LOR, extract flags
        sop_summary, sop_flags = summarize_sop_and_flags(sop_path)
        lor_summary, lor_flags = summarize_lor_and_flags(lor_path)

        # Score SOP and LOR based on keywords
        sop_score = score_sop(sop_summary)
        lor_score = score_lor(lor_summary)

        # Combine research flag from SOP or LOR
        research_flag = int(sop_flags['research'] or lor_flags['research'])

        # Prepare data for model prediction
        input_data = {
            'toefl_score': toefl_score,
            'university_rating': 5,
            'sop_score': sop_score,
            'lor_score': lor_score,
            'cgpa': cgpa_value,
            'research': research_flag
        }
        if gre_score is not None:
            input_data['gre_score'] = gre_score

        # Predict admission chance
        prediction = predict_admission_chance(**input_data)

        return render_template(
            'index.html',
            sop_summary=sop_summary,
            lor_summary=lor_summary,
            sop_score=sop_score,
            lor_score=lor_score,
            admit_chance=prediction['admit_chance'],
            classification=prediction['classification']
        )

    # GET request renders the upload form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
