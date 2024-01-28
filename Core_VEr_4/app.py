from flask import Flask, render_template, request, jsonify
from grammar_checker import correct_grammar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/api/grammar-check', methods=['POST'])
def grammar_check():
    data = request.get_json()
    input_text = data['text']

    # Perform grammar correction using the provided function
    corrected_text = correct_grammar(input_text)

    return jsonify({'result': corrected_text})

if __name__ == '__main__':
    app.run(debug=True)
