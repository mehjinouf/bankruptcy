#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pickle

# Load the saved model from a file
with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

st.title("Bankruptcy prediction")

Industrial_risk = ["High", "Intermediate", "Low"]
Management_risk = ["High", "Intermediate", "Low"]
Financial_flexibility = ["High", "Intermediate", "Low"]
Credibility = ["High", "Intermediate", "Low"]
Operating_risk = ["High", "Intermediate", "Low"]

input1 = st.selectbox("Industrial Risk:", Industrial_risk)
input2 = st.selectbox("Management Risk:", Management_risk)
input3 = st.selectbox("Financial Flexibility:", Financial_flexibility)
input4 = st.selectbox("Credibility:", Credibility)
input5 = st.selectbox("Operating Risk:", Operating_risk)

value1 = lambda x: 1 if len(x) == 4 else (0 if len(x) == 3 else 0.5)
V1 = list(map(value1, [input1]))

value2 = lambda x: 1 if len(x) == 4 else (0 if len(x) == 3 else 0.5)
V2 = list(map(value2, [input2]))

value3 = lambda x: 1 if len(x) == 4 else (0 if len(x) == 3 else 0.5)
V3 = list(map(value3, [input3]))

value4 = lambda x: 1 if len(x) == 4 else (0 if len(x) == 3 else 0.5)
V4 = list(map(value4, [input4]))

value5 = lambda x: 1 if len(x) == 4 else (0 if len(x) == 3 else 0.5)
V5 = list(map(value5, [input5]))

to_predict = [V1[0], V2[0], V3[0], V4[0], V5[0]]

if st.button("Predict"):
    predictions = loaded_model.predict([to_predict])
    if predictions == 1:
        st.write("No chance of getting Bankrupted")
    else:
        st.write("Chance of getting Bankrupted")


# In[ ]:




