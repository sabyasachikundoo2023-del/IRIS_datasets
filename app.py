import streamlit as st
import joblib
import numpy as np

# 1. Load the model
model = joblib.load('trained_model.pkl')

# 2. Page Configuration
st.set_page_config(page_title="Botanical Intelligence | Sabyasachi", page_icon="🌿", layout="wide")

# 3. Premium CSS (Cinematic Dark Theme)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500&display=swap');

    /* Global Dark Cinematic Palette */
    .stApp {
        background: radial-gradient(circle at top, #1c2a3d 0%, #0F1A2A 100%);
        color: #F5F5F5;
        font-family: 'Inter', sans-serif;
    }

    /* Fixed Navigation */
    .nav-bar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        padding: 1.5rem 4rem;
        background: rgba(15, 26, 42, 0.9);
        backdrop-filter: blur(10px);
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 999;
        border-bottom: 1px solid rgba(198, 167, 94, 0.2);
    }

    /* Hero Section */
    .hero-container {
        padding: 12rem 4rem 6rem 4rem;
        animation: fadeInUp 1.2s ease-out;
    }
    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: 5rem;
        color: #F5F5F5;
        line-height: 1.1;
        margin-bottom: 1.5rem;
        max-width: 800px;
    }
    .hero-subtitle {
        font-size: 1.1rem;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: #C6A75E; /* Muted Gold */
        margin-bottom: 2rem;
    }

    /* Refined Luxury Button */
    .stButton>button {
        background-color: transparent;
        color: #C6A75E !important;
        border: 1px solid #C6A75E;
        border-radius: 6px;
        padding: 1rem 3rem;
        font-weight: 500;
        letter-spacing: 0.1em;
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        width: auto;
    }
    .stButton>button:hover {
        background-color: #C6A75E;
        color: #0F1A2A !important;
        box-shadow: 0 0 20px rgba(198, 167, 94, 0.3);
    }

    /* Prediction Card */
    .prediction-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 4rem;
        border-radius: 8px;
        margin-top: 4rem;
        animation: slideUp 1s ease-out;
    }

    /* Animations */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(50px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Sidebar and Input Adjustment */
    [data-testid="stSidebar"] {
        background-color: #0B131E;
        border-right: 1px solid rgba(198, 167, 94, 0.1);
    }
    
    /* Elegant Footer */
    .luxury-footer {
        margin-top: 10rem;
        padding: 4rem;
        text-align: center;
        border-top: 1px solid rgba(198, 167, 94, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 4. Navigation
st.markdown("""
    <div class="nav-bar">
        <div style="letter-spacing: 0.2em; font-size: 0.8rem; font-weight: 500;">BOTANICAL INTELLIGENCE</div>
        <div style="font-size: 0.75rem; color: #C6A75E;">SABYASACHI KUNDOO</div>
    </div>
    """, unsafe_allow_html=True)

# 5. Hero Section
st.markdown("""
    <div class="hero-container">
        <div class="hero-subtitle">Ensemble Learning Workflow</div>
        <h1 class="hero-title">Precision in Botanical Intelligence</h1>
        <p style="max-width: 500px; color: #aaa; line-height: 1.8;">
            Harnessing the power of Random Forest architectures to identify 
            floral species with unparalleled statistical accuracy.
        </p>
    </div>
    """, unsafe_allow_html=True)

# 6. Interaction & Methodology Section
st.write("---")
col1, space, col2 = st.columns([1, 0.2, 1.2])

with col1:
    st.markdown("<h3 style='font-family: Playfair Display; color: #C6A75E;'>Parameters</h3>", unsafe_allow_html=True)
    st.write("Configure the sepal and petal dimensions for classification.")
    
    # Elegant Sliders in the Main Area
    sl = st.slider('Sepal Length', 4.3, 7.9, 5.8)
    sw = st.slider('Sepal Width', 2.0, 4.4, 3.0)
    pl = st.slider('Petal Length', 1.0, 6.9, 4.3)
    pw = st.slider('Petal Width', 0.1, 2.5, 1.3)
    
    input_data = np.array([[sl, sw, pl, pw]])
    
    predict_btn = st.button("RUN CLASSIFICATION")

with col2:
    st.markdown("<h3 style='font-family: Playfair Display; color: #C6A75E;'>The Methodology</h3>", unsafe_allow_html=True)
    st.markdown("""
        <div style="color: #aaa; line-height: 1.8; font-size: 0.95rem;">
        The system evaluates biological inputs against a matrix of 100 decision trees. 
        By calculating the mean probability across the Random Forest ensemble, 
        the model eliminates outliers and delivers a high-confidence species 
        identification. Developed as a showcase of end-to-end Machine Learning 
        pipelines in professional engineering environments.
        </div>
    """, unsafe_allow_html=True)
    
    if predict_btn:
        prediction = model.predict(input_data)
        prediction_proba = model.predict_proba(input_data)
        confidence = np.max(prediction_proba) * 100
        
        st.markdown(f"""
            <div class="prediction-card">
                <div style="letter-spacing: 0.3em; font-size: 0.65rem; color: #C6A75E; margin-bottom: 1rem;">IDENTIFIED SPECIMEN</div>
                <h2 style="font-family: 'Playfair Display', serif; font-size: 3rem; margin-bottom: 0.5rem;">Iris {prediction[0]}</h2>
                <p style="color: #666; font-size: 0.9rem;">Classification Confidence: {confidence:.2f}%</p>
            </div>
            """, unsafe_allow_html=True)

# 7. Cinematic Footer
st.markdown("""
    <div class="luxury-footer">
        <div style="text-transform: uppercase; letter-spacing: 0.3em; font-size: 0.7rem; color: #C6A75E; margin-bottom: 1.5rem;">Developed by Sabyasachi Kundoo</div>
        <div style="font-size: 0.75rem; color: #444;">© 2026 ALL RIGHTS RESERVED | MACHINE LEARNING PORTFOLIO</div>
    </div>
    """, unsafe_allow_html=True)
