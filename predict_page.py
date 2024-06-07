
import streamlit as st
import pickle
import numpy as np
import pandas as pd

def load_model():
    with open('diabetes-prediction-rfc-model.pkl','rb') as file:
        data = pickle.load(file)
    return data  

data = load_model()

def show_predict_page():
    st.title("Early Detection of Onset of Type-II diabetes")
    st.write("""### User Information""")
    sbp = st.text_input("Systolic BP", 0)
    dbp = st.text_input("Diastolic BP", 0)
    hr = st.text_input("Heart Rate", 0)
    glucose = st.text_input("Glucose", 0)
    age = st.text_input("Age", 0)
    temp = st.text_input("Body Temperature", 0)
    ok = st.button("Predict Pre-diabetes")
    if ok:
        dict = {'Age': [age],'Blood Glucose Level(BGL)': [glucose],'Diastolic Blood Pressure': [dbp],'Systolic Blood Pressure': [sbp],'Heart Rate': [hr],'Body Temperature': [temp]}
        test = pd.DataFrame(dict)
        predicted = data.predict(test)
        if predicted==1:
            st.subheader("YOU ARE AT A RISK OF PRE-DIABETES")
        else:
            st.subheader("YOU ARE NOT AT A RISK OF PRE-DIABETES")
    