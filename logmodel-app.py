#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pickle 
import numpy as np

model = pickle.load(open('logmodelml.pkl', 'rb'))


# In[2]:


def predict_carinsurance_buyer(Age, Previously_Insured, Gender_Male, Vehicle_Age_greater_2y, Vehicle_Damage_Yes, Vehicle_Age_less_1y):
    input = np.array([[Age, Previously_Insured, Gender_Male, Vehicle_Age_greater_2y, Vehicle_Damage_Yes, Vehicle_Age_less_1y]]).astype(np.float64)
    prediction = model.predict(input)
    return prediction


# In[3]:


def main():
    
    st.markdown('<style>body{background-color: White;}</style>',unsafe_allow_html=True)
    
    st.title('Predict if a Healthy insurance client would also buy a car insurance')
    st.write('''
    A healthy insurance company will launch a Vehicle insurance. They must know if their clients are prone to
    buy this car insurance or not. To answer this question, just put a few client informations below!
    ''')
    
    Age = st.text_input("Client Age:", "")
    Previously_Insured = st.text_input("Client have some previous insurance? (Yes - type 1, No - type 0)", "")
    Gender_Male = st.text_input("Client Gender: (Male - type 1, Female - type 0)", "")
    Vehicle_Age_less_1y = st.text_input("Does the client have a car with less than 1 year? (Yes - 1, No - 0)", "")
    Vehicle_Age_greater_2y = st.text_input("Does the client have a car with more than 2 years? (Yes - 1, No - 0)", "")
    Vehicle_Damage_Yes = st.text_input("Does the client have ever crashed a car before? (Yes - 1, No - 0)", "")
    
    probablybuyer_html = """
    <div style="background-color:#00B63C"; padding: 10px>
    <h2 style="color:white; text-align:center;">This client probably would buy a car insurance </h2>
    </div>
    """
    probablynotbuyer_html = """
    <div style="background-color:#F08080"; padding: 10px>
    <h2 style="color:black; text-align:center;">This client might not be interested in a car insurance </h2>
    </div>
    """
    
    if st.button("Predict"):
        output = predict_carinsurance_buyer(Age, Previously_Insured, Gender_Male, Vehicle_Age_greater_2y, Vehicle_Damage_Yes, Vehicle_Age_less_1y)
        
        if output == 1:
            st.markdown(probablybuyer_html, unsafe_allow_html=True)
        else:
            st.markdown(probablynotbuyer_html, unsafe_allow_html=True)
            
if __name__ == '__main__':
    main()

