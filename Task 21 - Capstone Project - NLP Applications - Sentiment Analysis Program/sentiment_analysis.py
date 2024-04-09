import spacy

import pandas as pd

from spacytextblob.spacytextblob import SpacyTextBlob   # Install spacytextblob using pip install spacytextblob

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

nlp.add_pipe('spacytextblob')  # Add spacytextblob for sentiment analysis

# Preprocess and clean text data in batches
def preprocess_texts(texts):
    # Process texts in batches for efficiency
    docs = list(nlp.pipe(texts, batch_size=50))
    cleaned_texts = []
    for doc in docs:
        # Remove stopwords, punctuation, and perform lemmatization
        cleaned_tokens = [token.lemma_.lower().strip() for token in doc if not token.is_stop and not token.is_punct and token.text.strip()]
        cleaned_texts.append(' '.join(cleaned_tokens))
    return cleaned_texts

# Perform sentiment analysis using spacytextblob
def analyze_sentiment(review_text):
    doc = nlp(review_text)
    # Determine sentiment based on polarity score from spacytextblob
    polarity = doc._.polarity
    return 'Positive' if polarity > 0 else 'Negative' if polarity < 0 else 'Neutral'

# Load datasets, preprocess texts, and apply sentiment analysis
file_paths = [
    r'C:\Users\Fierce\Desktop\New folder\1429_1.csv',
    r'C:\Users\Fierce\Desktop\New folder\Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products.csv',
    r'C:\Users\Fierce\Desktop\New folder\Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv'
]

dataframes = [pd.read_csv(path, low_memory=False) for path in file_paths]
for df in dataframes:
    df.dropna(subset=['reviews.text'], inplace=True)
    df['cleaned_reviews'] = preprocess_texts(df['reviews.text'].tolist())

# Test and display results for sentiment analysis on sample reviews
sample_reviews = dataframes[0]['reviews.text'].iloc[:5]
results = [analyze_sentiment(review) for review in sample_reviews]
for review, sentiment in zip(sample_reviews, results):
    print(f"Review: {review}\nSentiment: {sentiment}\n")

# Additional: Compare the similarity of two product reviews
review1 = nlp(dataframes[0]['reviews.text'].iloc[0])
review2 = nlp(dataframes[0]['reviews.text'].iloc[1])
similarity = review1.similarity(review2)
print(f"Similarity between two reviews: {similarity}")

# Note: Since spaCy's en_core_web_sm model doesn't have built-in sentiment analysis,
# the 'analyze_sentiment' function above is just a placeholder. For actual sentiment
# analysis, you might need to use a different library or model that supports sentiment scores.
