import streamlit as st
import joblib
import numpy as np

# 1. Load your trained Random Forest model
# Ensure 'trained_model.pkl' is in the same folder as this script
model = joblib.load('trained_model.pkl')

# 2. Set up the Page UI
st.set_page_config(page_title="Iris Species Predictor", page_icon="🌸")
st.title("🌸 Iris Flower Species Predictor")
st.markdown("""
This app uses a **Random Forest Classifier** to predict the species of an Iris flower based on its measurements.
""")

st.write("---")

# 3. Create Input Sliders (Based on Iris dataset features)
st.sidebar.header("Input Flower Measurements")

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal Length (cm)', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal Width (cm)', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal Length (cm)', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal Width (cm)', 0.1, 2.5, 0.2)
    
    data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    return data

input_df = user_input_features()

# Display the inputs to the user
st.subheader("Selected Measurements")
st.write(f"**Sepal:** {input_df[0][0]}cm x {input_df[0][1]}cm | **Petal:** {input_df[0][2]}cm x {input_df[0][3]}cm")

# 4. Prediction Logic
if st.button("Predict Species"):
    prediction = model.predict(input_df)
    
    # We remove the 'species' list entirely to avoid the TypeError
    st.write("---")
    st.subheader("Prediction Result")
    
    # This line works whether prediction[0] is an integer or a string
    st.success(f"The predicted species is: **Iris {prediction[0]}**")
    
    # Confidence level display
    prediction_proba = model.predict_proba(input_df)
    confidence = np.max(prediction_proba) * 100
    st.write(f"**Confidence Level:** {confidence:.2f}%")
