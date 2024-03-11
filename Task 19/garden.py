import spacy                        # Load the spacy library

nlp = spacy.load("en_core_web_sm")  # Load the small English model
gardenpathSentences = [             # A list of sentences that are difficult to parse
    "The old man the boat.",
    "The complex houses married and single soldiers and their families",
    "The horse raced past the barn fell.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

for sentence in gardenpathSentences: # Iterate over the sentences
    doc = nlp(sentence)              # Process the text with spacy
    print(f"Tokens in '{sentence}': {[token.text for token in doc]}") # Print the tokens
    print(f"Entities in '{sentence}': {[ent.text + ' (' + ent.label_ + ')' for ent in doc.ents]}") # Print the entities
    print()                         # Print a newline


unique_labels = set()  # Set to store unique entity labels

for sentence in gardenpathSentences:    # Iterate over the sentences
    doc = nlp(sentence)  # Process each sentence
    for ent in doc.ents:    # Iterate over the entities
        unique_labels.add(ent.label_)  # Add entity labels to the set

# Now, explain each unique entity label
for label in unique_labels: # Iterate over the unique labels
    explanation = spacy.explain(label)  # Get the explanation for the label
    print(f"{label}: {explanation}")    # Print the label and its explanation

# Comment on Entities:
# 1. PERSON (People, including fictional): This entity represents individuals or characters. In the context of "The old man the boat.", there was no PERSON entity identified, which initially might not make sense because 'old man' sounds like a person. However, correctly, 'old man' in this context is not an individual but part of an idiomatic expression, so the absence of a PERSON entity is justified.
# 2. GPE (Geopolitical Entities): In "The cotton clothing is made of grows in Mississippi", Mississippi is identified as a GPE, which is accurate and makes sense as it refers to the state where the cotton is grown.
