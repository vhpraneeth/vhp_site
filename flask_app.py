from flask import Flask, send_from_directory, abort  # , url_for, render_template
#from flask_weasyprint import render_pdf
from mail_sender import send_mail

app = Flask(__name__)


@app.route('/')
def index():
    return '''<a href=https://drive.google.com/file/d/1KDgWAz7DyN_bAFCHz-5-w3j1B0JHdLET/view> Visit this link for resume </a>'''
    #return render_template('index.html')


@app.route('/files/<path:path>',methods = ['GET','POST'])
def get_files(path):
    try:
        return send_from_directory("./files/", path, as_attachment=True)
    except FileNotFoundError:
        abort(404)


@app.route('/resume')
def get_pdf(name='Praneeth_Resume'):
    return '''<a href=https://drive.google.com/file/d/1KDgWAz7DyN_bAFCHz-5-w3j1B0JHdLET/view> Visit this link for resume </a>'''
    #return '<a href="files/Praneeth_Resume.pdf">My Resume</a>'
    #return render_pdf(url_for('files/Praneeth_Resume.pdf'))


if __name__ == '__main__':
    #app.secret_key = 'mysecret'
    app.run(debug=True)
