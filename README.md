🎓 Student Score Prediction System
📌 Project Overview

The Student Score Prediction System is a Machine Learning web application that predicts a student's final exam score based on various academic and personal factors.

The application is built using:

Python

NumPy

Scikit-Learn

Streamlit (for interactive web deployment)

This system helps estimate student performance using predictive modeling techniques.

🎯 Problem Statement

Educational institutions often need to identify student performance trends early in order to provide academic support. Manual evaluation can be time-consuming and subjective.

This project uses Machine Learning to predict final scores based on measurable inputs such as:

Age

Gender

Study Hours

Attendance Percentage

Past Exam Score

Internet Access

Participation in Extracurricular Activities

📊 Dataset

File: student_performance_dataset.csv

Contains structured student academic and demographic data.

Used for:

Data Cleaning

Exploratory Data Analysis (EDA)

Feature Engineering

Model Training

⚙️ Project Workflow
1️⃣ Data Understanding

Loaded dataset using Pandas

Performed exploratory data analysis

Checked for missing values and feature distributions

2️⃣ Data Preprocessing

Converted categorical features into numerical values

Selected relevant features for prediction

Structured dataset for model training

3️⃣ Model Training

Applied regression-based Machine Learning algorithm

Trained model on student performance data

Saved trained model as:

student_score_model.pkl

4️⃣ Deployment

Built interactive web interface using Streamlit

Integrated trained model for real-time prediction

Designed clean UI with background styling

🖥 Application Features

User-friendly input form

Real-time score prediction

Clean and professional UI

Error handling for model loading

Numeric output with precision formatting

📁 Project Structure
├── app.py
├── student_score_model.pkl
├── student_performance_dataset.csv
├── student.ipynb
└── README.md

🚀 How to Run the Project
1️⃣ Clone the Repository
git clone <your-repository-link>
cd <your-repository-name>

2️⃣ Install Required Libraries
pip install streamlit scikit-learn numpy pandas joblib

3️⃣ Run the Application
streamlit run app.py


The application will open automatically in your browser.

📈 Model Information

Type: Regression Model

Input Features: 7

Output: Predicted Final Score

Deployment Framework: Streamlit

🔮 Future Improvements

Add model performance metrics (R², MAE, RMSE)

Add data visualization dashboard

Deploy on Streamlit Cloud

Add authentication system for institutions

Improve model using advanced ensemble methods

👩‍💻 Author

Vijaya Jyothi Nersu
Aspiring Data Scientist | Machine Learning Enthusiast
