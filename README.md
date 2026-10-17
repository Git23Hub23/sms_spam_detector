# SMS Spam Detector

A machine learning web app that classifies SMS messages as **spam** or **ham** (not spam).

**Live demo:** (https://smsspamdetector-y7smfctxduqv8wn7vbgcwh.streamlit.app/)

## Problem
Spam messages waste time and can be scams. This project trains a model to detect them from the message text alone.

## Dataset
SMS Spam Collection (UCI / Kaggle), about 5,500 labeled messages.
After removing duplicates: 4,516 ham and 653 spam (spam is only about 12.6%, so the data is imbalanced).
After text cleaning, 5,128 messages remain.

## Approach
1. **Exploration:** spam messages are longer (about 138 vs 70 characters) and contain more digits and capital letters. Common spam words: free, call, txt, claim, prize, mobile.
2. **Cleaning:** lowercase, remove punctuation and numbers, remove stopwords, stemming.
3. **Features:** TF-IDF (top 3,000 words). Data split 80/20 with stratification, and the vectorizer was fitted on training data only to avoid data leakage.
4. **Models compared:** Naive Bayes, Logistic Regression, Linear SVM.
5. **Tuning:** GridSearchCV (5-fold, scored on F1) on Linear SVM.
6. **Deployment:** Streamlit app on Streamlit Community Cloud.

## Results
Model comparison (spam class, test set of 1,026 messages):

| Model | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| Naive Bayes | 0.9756 | 0.9907 | 0.8154 | 0.8945 |
| Logistic Regression | 0.9669 | 0.9898 | 0.7462 | 0.8509 |
| Linear SVM | 0.9834 | 0.9829 | 0.8846 | 0.9312 |

Best settings after tuning: `C=2`, `max_features=3000`, `ngram_range=(1,1)` (cross-validation F1 = 0.9131).

**Final model** (calibrated Linear SVM, takes raw text): accuracy 0.99, spam precision 0.98, recall 0.91, F1 0.94.

Accuracy alone is misleading here because always guessing "ham" already scores about 87%, so I focus on precision, recall and F1 for the spam class.

## Limitations
- The dataset is old, so the model works well on classic SMS spam (prizes, "call now") but can miss modern promotional messages, such as app marketing.
- The test set has only 130 spam messages, so small differences between models are a few messages.

## Tech stack
Python, pandas, scikit-learn, NLTK, Streamlit

## Project structure
- `data/`: dataset and cleaned data
- `notebooks/`: exploration, cleaning, TF-IDF, models, evaluation, tuning
- `models/spam_model.joblib`: saved model
- `preprocess.py`: text cleaning function
- `app.py`: Streamlit app

## How to run locally
```bash
git clone https://github.com/Git23Hub23/sms_spam_detector.git
cd sms_spam_detector
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Future improvements
- Add a more modern dataset to catch promotional messages
- Support Telugu / Hindi messages
- Show which words pushed a prediction towards spam