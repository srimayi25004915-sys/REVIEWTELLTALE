from collections import Counter
from reviewtelltale.cleaner import clean_text

def check_duplicates(reviews):
    cleaned_reviews = [clean_text(review) for review in reviews]

    counts = Counter(cleaned_reviews)

    duplicate_reviews = {}

    for review, count in counts.items():
        if review and count > 1:
            duplicate_reviews[review] = count

    return duplicate_reviews


def check_short_reviews(reviews):
    flagged = []

    for review in reviews:
        if len(clean_text(review).split()) <= 2:
            flagged.append(review)

    return flagged