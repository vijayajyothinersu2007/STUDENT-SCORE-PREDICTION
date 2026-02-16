import streamlit as st
import joblib
import numpy as np
import os

# -------- Page Config --------
st.set_page_config(
    page_title="Student Score Prediction",
    page_icon="🎓",
    layout="wide"
)

# -------- Full Background Image + Clean Overlay --------
image_url = "https://www.brookings.edu/wp-content/uploads/2025/04/shutterstock_2405355581-1.jpg?quality=75&w=1500"

st.markdown(f"""
<style>

[data-testid="stAppViewContainer"] {{
    background-image: url("{image_url}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

.form-container {{
    background: rgba(0, 0, 0, 0.65);
    padding: 40px;
    border-radius: 20px;
    width: 45%;
    margin: auto;
    margin-top: 80px;
    color: white;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.5);
}}

.form-container h1 {{
    text-align: center;
    margin-bottom: 10px;
}}

.form-container p {{
    text-align: center;
    margin-bottom: 30px;
    font-size: 18px;
}}

.stButton>button {{
    width: 100%;
    background-color: #4CAF50;
    color: white;
    font-weight: bold;
    border-radius: 12px;
    height: 45px;
}}

</style>
""", unsafe_allow_html=True)

# -------- Load Model Safely --------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "student_score_model.pkl")

try:
    model = joblib.load(model_path)
except Exception as e:
    st.error(f"Model loading failed: {e}")
    st.stop()

# -------- Overlay Form --------
st.markdown('<div class="form-container">', unsafe_allow_html=True)

st.markdown("<h1>🎓 Student Score Prediction System</h1>", unsafe_allow_html=True)
st.markdown("<p>Predict student academic performance using Machine Learning</p>", unsafe_allow_html=True)

# -------- Input Fields --------
age = st.number_input("Age", min_value=10, max_value=30, value=18)

gender = st.selectbox("Gender", ["Male", "Female"])
gender_numeric = 1 if gender == "Male" else 0

study = st.number_input(
    "Study Hours per Day", min_value=0.0, max_value=24.0, value=5.0, step=0.5
)

attendance = st.number_input(
    "Attendance Percentage", min_value=0.0, max_value=100.0, value=75.0, step=1.0
)

past = st.number_input(
    "Past Exam Score", min_value=0.0, max_value=100.0, value=70.0, step=1.0
)

internet = st.selectbox("Internet Access", ["Yes", "No"])
internet_numeric = 1 if internet == "Yes" else 0

extra = st.selectbox("Extracurricular Activities", ["Yes", "No"])
extra_numeric = 1 if extra == "Yes" else 0

# -------- Predict Button --------
if st.button("Predict Score"):
    try:
        input_data = np.array(
            [[
                age,
                gender_numeric,
                study,
                attendance,
                past,
                internet_numeric,
                extra_numeric
            ]],
            dtype=float
        )

        prediction = model.predict(input_data)

        st.success(f"✅ Predicted Final Score: {prediction[0]:.2f}")

    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")

st.markdown('</div>', unsafe_allow_html=True)
