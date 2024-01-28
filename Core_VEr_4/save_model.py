import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_lg")

# Specify the directory to save the model (create the 'model' folder if it doesn't exist)
model_directory = "model/"

# Save the spaCy model to the specified directory
nlp.to_disk(model_directory)
