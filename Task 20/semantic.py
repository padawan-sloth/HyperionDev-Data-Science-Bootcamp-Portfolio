import spacy

nlp = spacy.load('en_core_web_sm')

tokens = nlp('cat apple monkey banana')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Note on similarities:
# Analyzing "cat," "monkey," and "banana" using spaCy, "cat" and "monkey" are more similar, being animals. 
# "Banana" is less similar to both as it is a fruit, reflecting NLP's semantic understanding.
# Example: Comparing "bird" and "airplane" might show moderate similarity (both related to flying),
# whereas "bird" and "apple" would be less similar, demonstrating how NLP discerns context and category relations.


# Run the example file on with the simpler language model ‘en_core_web_sm’
# and write a note on what you notice may be different from the model 'en_core_web_md'
        
# The similarity scores are lower than those obtained using the 'en_core_web_md' model.
# This is because the 'en_core_web_md' model has a larger vocabulary and is more accurate in identifying similarities.
# The 'en_core_web_md' model is trained on more data and has a larger vocabulary, which makes it more accurate in identifying similarities.
# The 'en_core_web_md' model is more accurate in identifying similarities because it is trained on more data and has a larger vocabulary.
