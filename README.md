# SMS Spam Detector

A machine learning project that classifies SMS messages as **spam** or **ham** (not spam).

## Status
In progress (Day 5 of 10: first model trained)

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
After cleaning, 5,128 messages remain.

## Feature extraction
Text is converted to numbers using **TF-IDF** (top 3,000 words). The data is split 80% train / 20% test, and the vectorizer is fitted on training data only to avoid data leakage.

## Model
First model: **Multinomial Naive Bayes** trained on TF-IDF features.
- Accuracy: about 97% on the test set (write your exact number here).
- A model that always guesses "ham" scores about 87%, so accuracy alone is not enough. Precision, recall and F1 come next.

## Limitations
The dataset is old, so the model works well on classic SMS spam (prizes, "call now") but can miss modern promotional messages, such as app marketing.

## Tech stack
Python, pandas, scikit-learn, NLTK, Streamlit

## Planned steps
1. Explore the data (done)
2. Clean the text (done)
3. Convert text to numbers with TF-IDF (done)
4. Train the first model (done)
5. Evaluate and compare more models
6. Build a Streamlit web app
7. Deploy online

## How to run
Coming soon.