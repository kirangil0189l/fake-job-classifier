# Fake Job Classifier (ML + Streamlit Project)

This project detects fake job postings using machine learning and provides an interactive web interface using Streamlit.

# Live Demo

[Try the App](https://fake-job-classifier-d9bcrvavmswvkfhv6buwhp.streamlit.app/)

Paste a job description and find out if it's likely **real** or **fake**.

# Features

- Classifies job descriptions as real or fake using an ML model
- Trained on [Kaggle's Fake Job Postings Dataset](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction)
- Handles imbalanced data using SMOTE
- AUC score: **0.96**
- Built with: `scikit-learn`, `Streamlit`, `joblib`, `TF-IDF`
- Includes a live keyword-based fraud alert system

# Project Structure


fake-job-classifier/
 app/                        # Streamlit app
   --  app.py
   --  tfidf_vectorizer.pkl
   --  fake_job_classifier.pkl
   --   requirements.txt

 notebooks/                 # Model development notebook
      fake_job_classification.ipynb

README.md



# Getting Started

1. Clone or download this repository
2. Navigate to the `app/` folder
3. Install required packages:
  bash
   pip install -r requirements.txt
   
4. Run the Streamlit app:
   bash
   streamlit run app.py
   


# Model Info

- Dataset: [Kaggle - Fake Job Postings](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction)
- Vectorizer: TF-IDF (top 5000 features)
- Model: Logistic Regression
- Techniques: SMOTE for class imbalance
- AUC: ~0.96 on realistic test data



# Features

- Paste a job description and get a prediction (Real  / Fake )
- Fast and responsive UI

#Try the App Live

[Open Fake Job Detector](https://fake-job-classifier-d9bcrvavmswvkfhv6buwhp.streamlit.app/)

Paste a job description to check if it’s real or fake using an ML model trained on real data!

# Author

Sukhkirandeep Kaur Sidhu, Ph.D.
Email:sukhkirandeep.kaur@gmail.com
