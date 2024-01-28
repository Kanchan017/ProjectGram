from flask import Flask, request, jsonify
from your_model_script import correct_grammar

app = Flask(__name__)

@app.route('/api/grammar_correction', methods=['POST'])
def grammar_correction():
    data = request.get_json()
    text = data.get('text', '')
    num_return_sequences = data.get('num_return_sequences', 1)

    corrected_text = correct_grammar(text, num_return_sequences)

    return jsonify({'corrected_text': corrected_text})

if __name__ == '__main__':
    app.run(debug=True)
