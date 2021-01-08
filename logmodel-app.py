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
st.markdown('<style>body{background-color: White;}</style>',unsafe_allow_html=True)
    
st.title('Predict if a client is prone to buy a Car Insurance')
st.write('''
Give the informations requested below to see if a client is worth a cold call offering
''')

def yesno(param):
    if param =='Yes':
        return 1
    else:
        return 0

def selectcheckbox(a):
    if a == 'Male':
        return 1
    else:
        return 0
    
Age = st.text_input('Client´s age:','')   

st.write('Client´s Gender:')
a = st.checkbox("Male"), st.checkbox("Female"), st.checkbox("Not informed")
Gender_Male = yesno(a)
    
       
# gender_choice = st.selectbox('Cleint´s Gender:', 
#     ['Male','Female','Undefined', 'Not informed'])
# Gender_Male = selectcheckbox(gender_choice)

Previously_Insured = st.selectbox("Client have some previous insurance?", ['', 'Yes', 'No'])
Previously_Insured = yesno(Previously_Insured)

Vehicle_Age_greater_2y = st.selectbox('Client´s car age is greater than 2 years?', ['','Yes', 'No'])
Vehicle_Age_greater_2y = yesno(Vehicle_Age_greater_2y)

Vehicle_Age_less_1y = st.selectbox('Client´s car age is less than 1 year?', ['','Yes', 'No'])
Vehicle_Age_less_1y = yesno(Vehicle_Age_less_1y)

Vehicle_Damage_Yes = st.selectbox("Does the client have ever being on a car crash?", ['','Yes', 'No'])
Vehicle_Damage_Yes = yesno(Vehicle_Damage_Yes)

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
    if output ==1:
        st.markdown(probablybuyer_html, unsafe_allow_html=True)
    else:
        st.markdown(probablynotbuyer_html, unsafe_allow_html=True)
        
