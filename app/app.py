import streamlit as st
import joblib
import os

# Get absolute path to current file directory
BASE_DIR = os.path.dirname(__file__)

# Load the model and vectorizer using correct relative path
model = joblib.load(os.path.join(BASE_DIR, "fake_job_classifier.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "tfidf_vectorizer.pkl"))


st.set_page_config(page_title="Fake Job Classifier", layout="centered")

st.title("Fake Job Posting Detector")
st.markdown("Paste a job description below and the model will predict whether it's **real** or **fake**.")

job_desc = st.text_area("Enter Job Description:", height=250)

if st.button("Predict"):
    if job_desc.strip() == "":
        st.warning("Please enter a job description.")
    else:
        vect = vectorizer.transform([job_desc])
        prediction = model.predict(vect)[0]

        if prediction == 1:
            st.error("FAKE JOB DETECTED")
        else:
            st.success("REAL JOB POSTING")