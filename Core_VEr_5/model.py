from nltk import word_tokenize, pos_tag


def correct_sentence(sentence, errors):
    corrected_sentence = sentence

    for error in errors:
        words = word_tokenize(error)
        if len(words) == 5:  # Assuming format "Possible subject-verb agreement issue: {word1} {word2}"
            incorrect_word1, incorrect_word2 = words[4].split()
            pos_tag1 = pos_tag([incorrect_word1])[0][1]
            pos_tag2 = pos_tag([incorrect_word2])[0][1]

            # Find synonyms for the incorrect words
            synonyms1 = find_synonyms(incorrect_word1, get_wordnet_pos(pos_tag1))
            synonyms2 = find_synonyms(incorrect_word2, get_wordnet_pos(pos_tag2))

            # Replace the incorrect words with synonyms based on part-of-speech
            if synonyms1 and pos_tag1.startswith('V'):
                corrected_sentence = corrected_sentence.replace(incorrect_word1, synonyms1[0], 1)
            if synonyms2 and pos_tag2.startswith('V'):
                corrected_sentence = corrected_sentence.replace(incorrect_word2, synonyms2[0], 1)

    return corrected_sentence


if __name__ == "__main__":
    input_sentence = "The cat and dogs is playing in the garden."

    # Perform grammar check
    result = grammar_check(input_sentence)

    if result:
        print("Grammar Errors:")
        for error in result:
            print(f"- {error}")

        # Correct the sentence
        corrected_sentence = correct_sentence(input_sentence, result)
        print("\nCorrected Sentence:")
        print(corrected_sentence)
    else:
        print("No grammar errors found.")
