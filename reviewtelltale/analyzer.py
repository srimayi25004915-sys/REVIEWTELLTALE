from collections import Counter

from reviewtelltale.sentiment import analyze_sentiment
from reviewtelltale.integrity import check_duplicates, check_short_reviews
from reviewtelltale.complaints import detect_complaints


def analyze_reviews(reviews):

    sentiments = []
    complaint_counts = Counter()
    evidence = {}

    ratings = {}

    for item in reviews:
        review = item["review"]
        rating = float(item["rating"])

        sentiment = analyze_sentiment(review)
        complaints = detect_complaints(review)

        sentiments.append(sentiment)

        for category in complaints:
            if category != "General Feedback":
                complaint_counts[category] += 1

                evidence.setdefault(category, []).append(review)

                ratings.setdefault(category, []).append(rating)

    review_texts = [item["review"] for item in reviews]

    duplicates = check_duplicates(review_texts)
    short_reviews = check_short_reviews(review_texts)

    total = len(reviews)

    sentiment_summary = Counter(sentiments)

    issue_report = []

    for category, count in complaint_counts.most_common():

        average_rating = sum(ratings[category]) / len(ratings[category])

        # Transparent priority scoring
        score = count * (6 - average_rating)

        if score >= 10:
            priority = "High"
        elif score >= 5:
            priority = "Medium"
        else:
            priority = "Low"

        issue_report.append({
            "issue": category,
            "mentions": count,
            "average_rating": round(average_rating, 2),
            "priority_score": round(score, 2),
            "priority": priority,
            "evidence": evidence[category]
        })

    return {
        "total_reviews": total,
        "sentiments": dict(sentiment_summary),
        "duplicates": duplicates,
        "short_reviews": short_reviews,
        "issues": issue_report
    }