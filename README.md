# 🧾 PDF → Word Converter (Flask Web App)

A simple web app built with **Python Flask** to convert `.pdf` files into `.docx` format using the `pdf2docx` library.

## 🚀 Features
- Upload any PDF file and convert it into Word
- Clean, dark-themed Bootstrap UI
- Simple Flask backend
- Works locally or on cloud (Render, Heroku, etc.)

---

## 🧩 Installation

```bash
git clone https://github.com/<your-username>/pdf-to-word-converter.git
cd pdf-to-word-converter
python -m venv venv
venv\Scripts\activate    # for Windows
pip install -r requirements.txt
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

---

## 🌐 Deploy on GitHub / Render / Railway
- Push this repo to GitHub  
- Connect it to Render.com or Railway.app  
- Add a `build command`: `pip install -r requirements.txt`  
- Add a `start command`: `python app.py`

---

## 🛠️ Tech Stack
- Python (Flask)
- pdf2docx
- HTML, CSS, Bootstrap (Dark Theme)

---

## ⚠️ Note
Conversion quality may vary for scanned or image-based PDFs.
