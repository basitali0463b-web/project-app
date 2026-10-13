import streamlit as st
import joblib
import pandas as pd

# Model load karein
model = joblib.load('starbucks_model.joblib')

st.title("Starbucks Beverage Category Predictor")
st.write("Enter the nutritional details to predict the beverage category.")

# Yahan user inputs add karein (apne features ke mutabiq)
calories = st.number_input("Calories", min_value=0, max_value=500, value=100)
total_fat = st.number_input("Total Fat (g)", min_value=0.0, max_value=50.0, value=5.0)

if st.button("Predict"):
    # Input ko DataFrame mein convert karein (training features ke sath match karte hue)
    input_data = pd.DataFrame([[calories, total_fat]], columns=['Calories', 'Total Fat (g)'])
    
    # Prediction perform karein
    prediction = model.predict(input_data)
    st.success(f"Predicted Beverage Category: {prediction[0]}")