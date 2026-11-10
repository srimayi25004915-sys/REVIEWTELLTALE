from reviewtelltale.cleaner import clean_text

positive_words = {
    "good", "great", "excellent", "amazing",
    "love", "loved", "happy", "best", "perfect",
    "beautiful", "fast", "worth", "comfortable",
    "helpful", "wonderful"
}

negative_words = {
    "bad", "poor", "worst", "terrible",
    "hate", "hated", "late", "slow", "broken",
    "damaged", "disappointed", "expensive",
    "useless", "problem", "defective", "awful"
}


def analyze_sentiment(review):
    words = clean_text(review).split()

    positive_count = 0
    negative_count = 0

    negation_words = {"not", "never", "no"}

    for i, word in enumerate(words):

        previous_word = words[i - 1] if i > 0 else ""

        if word in positive_words:
            if previous_word in negation_words:
                negative_count += 1
            else:
                positive_count += 1

        elif word in negative_words:
            if previous_word in negation_words:
                positive_count += 1
            else:
                negative_count += 1

    if positive_count > negative_count:
        return "Positive"
    elif negative_count > positive_count:
        return "Negative"
    else:
        return "Neutral"