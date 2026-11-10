# ReviewTelltale
### Customer Review Intelligence Toolkit

**Every review leaves a signal.**

ReviewTelltale is a Python package that analyses customer reviews to identify sentiment, unusual review patterns and recurring customer complaints.

## Features

- Text cleaning and preprocessing
- Positive, negative and neutral sentiment classification
- Duplicate review detection
- Short review identification
- Complaint category detection
- Complaint priority scoring
- Evidence-based reporting

## Technologies Used

- Python
- Regular Expressions
- CSV
- Collections Module

## Project Structure

```text
REVIEWLENS/
├── data/
│   └── sample_reviews.csv
├── reviewtelltale/
│   ├── __init__.py
│   ├── cleaner.py
│   ├── sentiment.py
│   ├── integrity.py
│   ├── complaints.py
│   └── analyzer.py
├── demo.py
└── README.md
```

## How to Run

1. Clone or download the repository.
2. Open the project folder in VS Code.
3. Run:

```bash
python demo.py
```

## How It Works

ReviewTelltale reads customer reviews from a CSV dataset and analyses them using different Python modules.

It generates a report containing sentiment summaries, duplicate review flags, complaint categories, priority scores and supporting review examples.

## Limitations

- Sentiment analysis uses predefined keywords.
- Duplicate and short reviews are flagged for inspection, not labelled as fake.
- Priority scores are custom heuristic scores, not validated business metrics.

## Future Improvements

- Advanced Natural Language Processing
- Machine Learning-based sentiment analysis
- Review similarity detection
- Data visualisation dashboards
- SQL database integration

## Author

Developed as a Python package project.