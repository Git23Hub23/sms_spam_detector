# SMS Spam Detector

A machine learning project that classifies SMS messages as **spam** or **ham** (not spam).

## Status
In progress (Day 3 of 10: text cleaning done)

## Dataset
SMS Spam Collection Dataset (UCI / Kaggle), about 5,500 labeled messages.
After removing duplicates: 4,516 ham and 653 spam.

## What I found so far
- Spam is only about 12.6% of the data (imbalanced).
- Spam messages are longer (about 138 characters) than normal messages (about 70).
- Spam contains more digits (phone numbers, prize codes) and more capital letters.
- Common spam words: free, call, txt, claim, prize, mobile.

## Text cleaning
Each message goes through these steps:
1. Convert to lowercase
2. Remove punctuation and numbers
3. Remove stopwords (the, is, and...)
4. Stemming (winning, winner, wins become "win")

Labels are converted to numbers: ham = 0, spam = 1.

## Tech stack
Python, pandas, scikit-learn, NLTK, Streamlit

## Planned steps
1. Explore the data (done)
2. Clean the text (done)
3. Convert text to numbers (TF-IDF)
4. Train and compare models
5. Build a Streamlit web app
6. Deploy online

## How to run
Coming soon.