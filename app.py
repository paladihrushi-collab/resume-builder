from flask import Flask, render_template, request, send_file
from xhtml2pdf import pisa
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.form.to_dict()   # Collect form data
    html = render_template('resume_template.html', data=data)

    pdf = BytesIO()
    pisa.CreatePDF(html, dest=pdf)  # <-- pass html string directly
    pdf.seek(0)

    return send_file(pdf, download_name="resume.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

