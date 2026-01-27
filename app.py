import streamlit as st
import joblib
import numpy as np
import os

# -------- Page Config --------
st.set_page_config(
    page_title="Student Score Prediction",
    page_icon="🎓",
    layout="centered"
)

# -------- Load Model Safely --------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "student_score_model.pkl")

try:
    model = joblib.load(model_path)
except Exception as e:
    st.error(f"Model loading failed: {e}")
    st.stop()

# -------- UI --------
st.title("🎓 Student Score Prediction System")
st.write("Enter student details to predict the final score.")

# -------- Input Features --------
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

# -------- Predict --------
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
        st.success(f"✅ Predicted Final Score: **{prediction[0]:.2f}**")

    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
