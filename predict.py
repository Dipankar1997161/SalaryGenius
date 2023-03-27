import streamlit as st
import pickle
import numpy as np
def load_model():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

regressor = model["model"]
en_country = model["country"]
en_education = model["education"]
                 
                 
def predict_page():
          
    countries = (
    "United States of America",
    "India",
    "United Kingdom of Great Britain and Northern Ireland",
    "Germany",
    "Canada",
    "Brazil",
    "France",
    "Spain",
    "Australia",
    "Netherlands",
    "Poland",
    "Italy",
    "Russian Federation",
    "Sweden",
    "Israel",
      "Switzerland",
      "Norway"
    )
    education = (
        "Pre Bachelors",
        "Bachelors",
        "Masters",
        "Postgrad",
    )
    education = st.selectbox("Education", education)
    country = st.selectbox("Country", countries)
    experience = st.slider("Years of Coding Experience",0,30,2)
    ok = st.button("Predict Your Salary")
    if ok:
        X =np.array([[education, country, experience]])
        X[:, 0] = en_education.transform(X[:,0])
        X[:, 1] = en_country.transform(X[:,1])
        X = X.astype(float)
        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")