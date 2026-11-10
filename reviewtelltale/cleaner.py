import re

def clean_text(text):

    # Convert text to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)

    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Return cleaned text
    return text.strip()

# Testing the function

review = " AMAZING Product!!! Loved it 😍 Visit www.example.com "

result = clean_text(review)

print("Original Review:", review)
print("Cleaned Review:", result)