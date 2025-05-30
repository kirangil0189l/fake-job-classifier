# Fake Job Classifier (ML + Streamlit Project)

This project detects fake job postings using machine learning and provides an interactive web interface using Streamlit.


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
- Perfect for resumes and demo purposes


# Author

Sukhkirandeep Kaur Sidhu, Ph.D.
Email:sukhkirandeep.kaur@gmail.com
