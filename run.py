from flask import Flask, request, render_template
import os
from werkzeug.utils import secure_filename
from parser.resume_parser import extract_text_from_pdf
from utils.helpers import match_skills

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'resume' not in request.files:
        return "No file part"
    file = request.files['resume']
    if file.filename == '':
        return "No selected file"
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        if filename.lower().endswith('.pdf'):
            extracted_text = extract_text_from_pdf(file_path)
            required_skills = ['python', 'sql', 'machine learning', 'flask', 'aws']
            matched = match_skills(extracted_text, required_skills)

            resume_score = int((len(matched) / len(required_skills)) * 100)
            return render_template('result.html', matched_skills=matched, text=extracted_text, score=resume_score)
        else:
            return "Unsupported file format. Only PDF supported right now."

if __name__ == '__main__':
    app.run(debug=True)
