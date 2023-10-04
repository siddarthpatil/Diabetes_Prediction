import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
import pickle
import numpy as np
st.title('Wee Deployment of Diabetes app')
st.subheader('Is the person diabetic or not?')
data = pd.read_csv('diabetes.csv')
st.set_option('deprecation.showPyplotGlobalUse', False)
if st.sidebar.checkbox('View Data',False):
    st.write(data)
if st.sidebar.checkbox('View Graph',False):
    data.hist()
    #plt.tight_layout()
    #st.pyplot()

# Load the pickle file
model = open('rfc.pickle','rb')
clf = pickle.load(model)
model.close()

# Get the front end user input
pregs = st.slider('Pregnancies',min(data['Pregnancies']),max(data['Pregnancies']),min(data['Pregnancies'])),
glucode = st.slider('Glucose',min(data['Glucose']),max(data['Glucose']),min(data['Glucose'])),
bp = st.slider('BloodPressure',data['BloodPressure'].min(),data['BloodPressure'].max(),data['BloodPressure'].min()),
skin = st.slider('SkinThickness',(min(data['SkinThickness'])),(max(data['SkinThickness'])),(min(data['SkinThickness']))),
insulin = st.slider('Insulin',min(data['Insulin']),max(data['Insulin']),min(data['Insulin'])),
bmi = st.slider('BMI',min(data['BMI']),max(data['BMI']),min(data['BMI'])),
diab = st.slider('DiabetesPedigreeFunction',min(data['DiabetesPedigreeFunction']),max(data['DiabetesPedigreeFunction']),min(data['DiabetesPedigreeFunction'])),
age = st.slider('Age',min(data['Age']),max(data['Age']),min(data['Age']))

# user input as model input
data = {
    'Pregnancies':pregs,
    'Glucose':glucode,
    'BloodPressure':bp,
    'SkinThickness':skin,
    'Insulin':insulin,
    'BMI':bmi,
    'DiabetesPedigreeFunction':diab,
    'Age':age
}

input_data = pd.DataFrame(data,index=[0])

# Predict the output
    
if st.button('Predict'):
    output = clf.predict(input_data)
    if output == 0:
        output = clf.predict(input_data)
    if output == 1:
        st.success('The person is diabetic')
    else:
        st.success('The person is not diabetic')
