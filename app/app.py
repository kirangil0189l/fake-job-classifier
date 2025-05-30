import streamlit as st
import joblib

# Load model and vectorizer
import os

model = joblib.load(os.path.join(os.path.dirname(__file__), "fake_job_classifier.pkl"))
vectorizer = joblib.load(os.path.join(os.path.dirname(__file__), "tfidf_vectorizer.pkl"))


st.set_page_config(page_title="Fake Job Classifier", layout="centered")

st.title("🕵️‍♂️ Fake Job Posting Detector")
st.markdown("Paste a job description below and the model will predict whether it's **real** or **fake**.")

job_desc = st.text_area("Enter Job Description:", height=250)

if st.button("Predict"):
    if job_desc.strip() == "":
        st.warning("Please enter a job description.")
    else:
        vect = vectorizer.transform([job_desc])
        prediction = model.predict(vect)[0]

        if prediction == 1:
            st.error("🚨 FAKE JOB DETECTED")
        else:
            st.success("✅ REAL JOB POSTING")