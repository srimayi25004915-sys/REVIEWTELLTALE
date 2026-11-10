from reviewtelltale.cleaner import clean_text

complaint_keywords = {
    "Delivery": ["delivery", "shipping", "late", "delay"],
    "Product Quality": ["broken", "damaged", "defective", "faulty"],
    "Packaging": ["packaging", "package", "box", "wrapped"],
    "Customer Service": ["service", "support", "staff", "response"],
    "Price": ["expensive", "price", "cost", "overpriced"],
    "Returns": ["return", "refund", "replacement", "exchange"]
}

def detect_complaints(review):
    words = clean_text(review).split()

    detected = []

    for category, keywords in complaint_keywords.items():
        if any(word in words for word in keywords):
            detected.append(category)

    if not detected:
        detected.append("General Feedback")

    return detected