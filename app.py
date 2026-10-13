import streamlit as st
import joblib
import pandas as pd

# Model load karein
model = joblib.load('starbucks_model.joblib')

st.title("Starbucks Beverage Category Predictor")
st.write("Enter the nutritional details to predict the beverage category.")

# User inputs for all required features
calories = st.number_input("Calories", value=100)
fat = st.number_input("Fat (g)", value=0.0)
trans_fat = st.number_input("Trans Fat (g)", value=0.0)
saturated_fat = st.number_input("Saturated Fat (g)", value=0.0)
sodium = st.number_input("Sodium (mg)", value=0)
carbs = st.number_input("Carbs (g)", value=0)
fiber = st.number_input("Fiber (g)", value=0.0)
sugar = st.number_input("Sugar (g)", value=0.0)
protein = st.number_input("Protein (g)", value=0.0)
caffeine = st.number_input("Caffeine (mg)", value=0.0)

if st.button("Predict"):
    # Training features ke mutabiq dataframe banayein
    input_data = pd.DataFrame([[
        calories, fat, trans_fat, saturated_fat, sodium, 
        carbs, fiber, sugar, protein, caffeine
    ]], columns=[
        'Calories', 'Fat (g)', 'Trans Fat (g)', 'Saturated Fat (g)', 'Sodium (mg)', 
        'Carb. (g)', 'Fiber (g)', 'Sugar (g)', 'Protein (g)', 'Caffeine (mg)'
    ])
    
    # Prediction perform karein
    prediction = model.predict(input_data)
    st.success(f"Predicted Beverage Category: {prediction[0]}")
