import spacy
import language_tool_python

# Load English tokenizer, tagger, parser, and NER for spaCy
nlp = spacy.load("en_core_web_lg")

# Create a LanguageTool instance for grammar correction
tool = language_tool_python.LanguageTool('en-US')


def correct_grammar(sentence):
    # Process the input sentence with spaCy
    doc = nlp(sentence)

    # Convert spaCy Doc to plain text for language_tool_python
    plain_text = ' '.join([token.text for token in doc])

    # Use language_tool_python for grammar correction
    matches = tool.check(plain_text)

    # Apply corrections to the plain text
    corrected_text = tool.correct(plain_text)

    return corrected_text


# Example usage with a new sentence
incorrect_sentence = "i has a cat"
corrected_sentence = correct_grammar(incorrect_sentence)
print("Incorrect:", incorrect_sentence)
print("Corrected:", corrected_sentence)