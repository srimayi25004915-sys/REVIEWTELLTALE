from reviewtelltale.complaints import detect_complaints
from reviewtelltale.sentiment import analyze_sentiment
from reviewtelltale.integrity import check_short_reviews

test_reviews = [
    "The delivery was very late.",
    "The product has good quality.",
    "The product is broken and damaged.",
    "Not good at all.",
    "",
    "Good",
    "Excellent product, loved it!"
]

print("========== EDGE CASE TESTING ==========")

for review in test_reviews:
    print("\nReview:", repr(review))
    print("Sentiment:", analyze_sentiment(review))
    print("Complaints:", detect_complaints(review))

print("\n--- SHORT REVIEW TEST ---")
print(check_short_reviews(test_reviews))

print("\n========== TESTING COMPLETE ==========")