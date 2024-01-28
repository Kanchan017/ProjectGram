import spacy
import language_tool_python
from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder=os.path.abspath('templates'))

# Load English tokenizer,ger, parser, NER for spaCy
nlp = spacy.load("en_core_web_lg")

# Create a LanguageTool instance for grammar correction
tool = language_tool_python.LanguageTool('en-US')


def correct_grammar(text: str) -> str:
    """
    Correct the grammar of the given text using spaCy and language_tool_python.
    """
    # Process the input sentence with spaCy
    doc = nlp(text)

    # Convert spaCy Doc to plain text for language_tool_python
    plain_text = ' '.join([token.text for token in doc])

    # Use language_tool_python for grammar correction
    matches = tool.check(plain_text)

    # Apply corrections to the plain text
    corrected_text = tool.correct(plain_text)

    # Add appropriate punctuation if needed
    corrected_text = add_punctuation(text, corrected_text)

    return corrected_text


def add_punctuation(original_text: str, corrected_text: str) -> str:
    """
    Add appropriate punctuation to the corrected text based on the original text.
    """
    # Check if the original sentence has punctuation
    if any(char in '.,;:!?' for char in original_text):
        return corrected_text

    # Add a period at the end if no punctuation is present
    if not corrected_text.endswith(('.', '!', '?')):
        corrected_text += '.'

    # Ensure the corrected sentence starts with a capital letter
    corrected_text = corrected_text[0].upper() + corrected_text[1:]

    # Fix possessive forms dynamically
    words = corrected_text.split()
    for i in range(len(words) - 1):
        if words[i].endswith('s') and words[i + 1].istitle():
            words[i] += "'"

    return ' '.join(words)


# Example usage with the new sentence
incorrect_sentence = "i has a cat"
corrected_sentence = correct_grammar(incorrect_sentence)
print("Incorrect:", incorrect_sentence)
print("Corrected:", corrected_sentence)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/grammar', methods=['POST'])
def grammar():
    if request.method == 'POST':
        input_text = request.form['text']
        corrected_text = correct_grammar(input_text)
        return render_template('index.html', input_text=input_text, corrected_text=corrected_text)


if __name__ == '__main__':
    app.run(debug=True)