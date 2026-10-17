# SMS Spam Detector

A machine learning project that classifies SMS messages as **spam** or **ham** (not spam).

## Status
In progress (Day 1 of 10: data loading and exploration done)

## Dataset
SMS Spam Collection Dataset (UCI / Kaggle), about 5,500 labeled messages.
After removing duplicates: 4,516 ham and 653 spam.

## What I found so far
- Spam is only about 12.6% of the data (imbalanced).
- Spam messages are longer on average (about 138 characters) than normal messages (about 70).

## Tech stack
Python, pandas, scikit-learn, Streamlit

## Planned steps
1. Explore the data
2. Clean the text
3. Convert text to numbers (TF-IDF)
4. Train and compare models
5. Build a Streamlit web app
6. Deploy online

## How to run?