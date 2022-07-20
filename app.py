import streamlit as st
import pandas as pd


st.write("""
# Find largest among 3 numbers App

This app finds the largest among 3 given numbers (value greater than the other two).
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    first_number = st.number_input("FIRST NUMBER",min_value=0.0,max_value=1000000000000.0,step=1.0)
    second_number = st.number_input("SECOND NUMBER",min_value=0.0,max_value=100000000000.0,step=1.0)
    third_number = st.number_input("THIRD NUMBER",min_value=0.0,max_value=10000000000.0,step=1.0)
    
    data = {'FIRST NUMBER': first_number,
            'SECOND NUMBER': second_number,
            'THIRD NUMBER': third_number,
            }
    features = data
    return features

features = user_input_features()

st.subheader('User Input parameters')
st.write(features)

first_number = features['FIRST NUMBER']
second_number = features['SECOND NUMBER']
third_number = features['THIRD NUMBER']
#Preprocessing

st.subheader('Largest Among given Numbers: ')
if first_number >= second_number and first_number >= third_number:
    st.write(first_number)
elif second_number >= first_number and second_number >= third_number:
    st.write(second_number)
else:
    st.write(third_number)
#st.write(prediction)

st.write('Thank you for trying our app!')
