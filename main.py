import pickle
import streamlit as st
import numpy as np
# Load the model
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)



st.title('Machine Failure Prediction')


footfall = st.number_input('Footfall', value=0.0)
tempMode = st.number_input('Temperature Mode', value=0.0)
AQ = st.number_input('Air Quality (AQ)', value=0.0)
USS = st.number_input('Usage Sensor Status (USS)', value=0.0)
CS = st.number_input('Cooling System (CS)', value=0.0)
VOC = st.number_input('Volatile Organic Compounds (VOC)', value=0.0)
RP = st.number_input('Repair Probability (RP)', value=0.0)
IP = st.number_input('Inspection Probability (IP)', value=0.0)
Temperature = st.number_input('Temperature', value=0.0)





if st.button('Predict Machine Failure'):
    # Prepare the input array
    input_data = np.array([[footfall, tempMode, AQ, USS, CS, VOC, RP, IP, Temperature]])
    
    # Make the prediction
    prediction = model.predict(input_data)
    
    # Output the result
    if prediction[0] == 1:
        st.error('The machine will fail.')
    else:
        st.success('The machine will not fail.')



#res = model.predict([[-0.27889869,  1.21515264,  0.45547176,  0.0237942 ,  0.46684025,0.97948605,  2.09636786, -0.99807045, -1.72116615]])

#print(res[0])
