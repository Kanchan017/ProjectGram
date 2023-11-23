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

    # Add appropriate punctuation if needed
    corrected_text = add_punctuation(sentence, corrected_text)

    return corrected_text


def add_punctuation(original_sentence, corrected_sentence):
    # Check if the original sentence has punctuation
    if any(char in '.,;:?!' for char in original_sentence):
        # Use the original sentence's punctuation
        return corrected_sentence
    else:
        # Check if the corrected sentence ends with appropriate punctuation
        if not corrected_sentence.endswith(('.', '!', '?')):
            # Add a period at the end if no punctuation is present
            corrected_sentence += '.'

        # Ensure the corrected sentence starts with a capital letter
        corrected_sentence = corrected_sentence.capitalize()

        # Fix possessive forms dynamically
        words = corrected_sentence.split()
        for i in range(len(words) - 1):
            if words[i].endswith('s') and words[i + 1].istitle():
                words[i] += "'"

        return ' '.join(words)


# Example usage with the new sentence
incorrect_sentence = "i has a cat"
corrected_sentence = correct_grammar(incorrect_sentence)
print("Incorrect:", incorrect_sentence)
print("Corrected:", corrected_sentence)