import streamlit as st
import pandas as pd
import pickle as pk

with open('Covid_Classification.pickle', 'rb') as f:
    model = pk.load(f)

st.title("Covid prediction")
Cough_symptoms = st.selectbox("Cough", (True, False))
Fever = st.selectbox("Fever", (True, False))
Sore_throat = st.selectbox("Sore Throat", (True, False))
Shortness_of_breath = st.selectbox("Shortness of Breath", (True, False))
Headache = st.selectbox("Headache", (True, False))
Known_contact = st.selectbox(
    "known Contact", ['Abroad', 'Contact with confirmed', 'Other'])
if st.button('Submit'):
    st.success('Form submitted Successfully')

    if Known_contact == 'Abroad':
        Known_contact = 0
    elif Known_contact == 'Contact with confirmed':
        Known_contact = 1
    else:
        Known_contact = 2

    data = {'Cough_symptoms': [Cough_symptoms], 'Fever': [Fever], 'Sore_throat': [Sore_throat], 'Shortness_of_breath': [
        Shortness_of_breath], 'Headache': [Headache], 'Known_contact': [Known_contact]}
    df = pd.DataFrame(data)
    result = model.predict(df)[0]
    if result == 1:
        result = 'Yes'
    else:
        result = 'No'
    st.write(f"Covid Prediction : {result}")
