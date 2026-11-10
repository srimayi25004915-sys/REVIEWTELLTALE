import csv
from reviewtelltale.analyzer import analyze_reviews

reviews = []

with open("data/sample_reviews.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        reviews.append({
            "review": row["review"],
            "rating": row["rating"]
        })

report = analyze_reviews(reviews)

print("\n========== REVIEWTELLTALE ==========")
print("CUSTOMER REVIEW INTELLIGENCE TOOLKIT")
print("===================================\n")

print("Total Reviews:", report["total_reviews"])

print("\n--- SENTIMENT ANALYSIS ---")
for sentiment, count in report["sentiments"].items():
    print(sentiment, ":", count)

print("\n--- REVIEW INTEGRITY ---")
print("Duplicate Reviews:", len(report["duplicates"]))
print("Short Reviews:", len(report["short_reviews"]))

for review, count in report["duplicates"].items():
    print("Repeated:", review, "| Count:", count)

print("\n--- COMPLAINT INTELLIGENCE ---")

for issue in report["issues"]:
    print("\nIssue:", issue["issue"])
    print("Mentions:", issue["mentions"])
    print("Average Rating:", issue["average_rating"])
    print("Priority Score:", issue["priority_score"])
    print("Priority:", issue["priority"])

    print("Supporting Evidence:")
    for example in issue["evidence"][:2]:
        print("-", example)

print("\n========== ANALYSIS COMPLETE ==========")