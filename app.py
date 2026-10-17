import os
import joblib
import streamlit as st
from preprocess import clean_text  # needed so the saved model can load

BASE = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(page_title="SMS Spam Detector", page_icon="📩")


@st.cache_resource
def load_model():
    return joblib.load(os.path.join(BASE, "models", "spam_model.joblib"))


model = load_model()

st.title("📩 SMS Spam Detector")
st.write("Paste an SMS message and the model will tell you if it looks like spam.")

examples = {
    "Spam example": "WINNER!! You have won a £900 prize. Call 09061701461 to claim now",
    "Normal example": "Hey, are we meeting for lunch tomorrow?",
}

if "msg" not in st.session_state:
    st.session_state.msg = ""

col1, col2 = st.columns(2)
if col1.button("Try a spam example"):
    st.session_state.msg = examples["Spam example"]
if col2.button("Try a normal example"):
    st.session_state.msg = examples["Normal example"]

text = st.text_area("Your message", key="msg", height=120)

if st.button("Predict", type="primary"):
    if not text.strip():
        st.warning("Please type or paste a message first.")
    else:
        prob = model.predict_proba([text])[0][1]
        if prob > 0.5:
            st.error(f"🚨 SPAM (spam probability: {prob:.0%})")
        else:
            st.success(f"✅ NOT SPAM (spam probability: {prob:.0%})")
        st.progress(float(prob))

st.caption(
    "Trained on the classic SMS Spam Collection dataset, so it works best on "
    "traditional SMS spam (prizes, 'call now') and may miss modern promotional messages."
)