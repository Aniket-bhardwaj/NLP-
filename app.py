from flask import Flask, request, render_template, redirect, url_for
import spacy
from spacy import displacy

my_nlp = spacy.load('en_core_web_sm')

my_app = Flask(__name__)

@my_app.route('/')
def my_index():
    return render_template('index.html')

@my_app.route('/analyze_entity', methods=['POST', 'GET'])
def analyze_entity():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file and uploaded_file.filename:  
            file_contents = uploaded_file.read().decode('utf-8', errors='ignore')
            analyzed_docs = my_nlp(file_contents)
            analyzed_html = displacy.render(analyzed_docs, style='ent', jupyter=False)
            return render_template('index.html', html=analyzed_html, text=file_contents)
        else:
            return render_template('index.html', upload_message='Please upload a file.')

@my_app.route('/reset_analysis')
def reset_analysis():
    return redirect(url_for('my_index'))

if __name__ == '__main__':
    my_app.run(debug=True)
