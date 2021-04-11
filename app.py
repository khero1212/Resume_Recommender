import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
import pickle
from classify import *
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


UPLOAD_FOLDER = os.path.abspath(".")

ALLOWED_EXTENSIONS = {'pdf'}
def allowed_file(filename):
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
       if 'file' not in request.files:
           print('No file attached in request')
           return redirect(request.url)
       file = request.files['file']
       if file.filename == '':
           print('No file selected')
           return redirect(request.url)
       if file and allowed_file(file.filename):
           filename = secure_filename(file.filename)
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
           file.save(file_path)
           test_text = convert_to_text(file_path)
           Model = pickle.load(open("model.pkl", "rb"))
           #count_vect = CountVectorizer()
           prediction =  Model.predict(count_vect.transform([test_text]))
           return prediction[0]

   return render_template('index.html')

def convert_to_text(file_path):
    return get_processed_text(file_path)

if __name__ == '__main__':
    app.run()
