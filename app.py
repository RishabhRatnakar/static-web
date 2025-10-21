from flask import Flask, request, send_file, render_template_string
from pdf2docx import Converter
import os, tempfile

app = Flask(__name__)

@app.route('/')
def home():
    with open('index.html', 'r', encoding='utf-8') as f:
        return render_template_string(f.read())

@app.route('/convert', methods=['POST'])
def convert():
    uploaded = request.files.get('file')
    if not uploaded or not uploaded.filename.endswith('.pdf'):
        return 'Invalid file', 400

    with tempfile.TemporaryDirectory() as tmpdir:
        pdf_path = os.path.join(tmpdir, 'input.pdf')
        docx_path = os.path.join(tmpdir, 'output.docx')
        uploaded.save(pdf_path)

        try:
            cv = Converter(pdf_path)
            cv.convert(docx_path, start=0, end=None)
            cv.close()
        except Exception as e:
            return f'Conversion failed: {e}', 500

        return send_file(docx_path, as_attachment=True, download_name='converted.docx')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
