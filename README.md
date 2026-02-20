# 🏭 Manufacturing Equipment Output Prediction System

## 📌 Capstone Project – Machine Learning + FastAPI + Streamlit

This project predicts the **number of parts produced per hour (Parts_Per_Hour)** in a manufacturing environment using Machine Learning. The system analyzes various machine and environmental parameters to estimate production output and improve operational efficiency.

This is a complete end-to-end ML project that integrates:

- 📊 Data Exploration & Preprocessing
- 🧠 Machine Learning Model Training
- ⚙️ FastAPI Backend (Model Serving)
- 🖥️ Streamlit Frontend (User Interface)

---

# 🎯 Problem Statement

In manufacturing industries, production output depends on multiple factors such as machine temperature, pressure, cycle time, material properties, and operator efficiency.

Manually optimizing these parameters is difficult.

The objective of this project is to:

> Predict hourly production output (Parts_Per_Hour) using machine operating parameters.

This helps companies:
- Improve efficiency
- Optimize machine settings
- Reduce downtime
- Support data-driven decision making

---

# 📊 Dataset Information

- Total Samples: 1000
- Total Features: 17
- Target Variable: Parts_Per_Hour
- Type of Problem: Regression

### Important Features Used

- Injection_Temperature
- Injection_Pressure
- Cycle_Time
- Cooling_Time
- Material_Viscosity
- Ambient_Temperature
- Machine_Age
- Operator_Experience
- Maintenance_Hours
- Machine_Utilization
- Efficiency_Score

---

# 🧠 Machine Learning Approach

## Algorithm Used
Linear Regression

## Why Linear Regression?

- Suitable for continuous output prediction
- Easy to interpret
- Helps understand feature importance
- Fast and efficient for real-time systems

---

# ⚙️ Project Workflow

## 1️⃣ Data Exploration
- Understanding dataset structure
- Checking missing values
- Correlation analysis
- Feature understanding

Notebook: `01_data_exploration.ipynb`

---

## 2️⃣ Data Preprocessing
- Handling missing values
- Encoding categorical variables
- Feature scaling using StandardScaler
- Train-test split

Notebook: `02_data_preprocessing.ipynb`

---

## 3️⃣ Model Training
- Training Linear Regression model
- Feature coefficient analysis
- Saving model using Joblib

Notebook: `03_model_training.ipynb`

---

## 4️⃣ Model Evaluation

Metrics Used:
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

Performance Achieved:
- R² Score: 0.90
- Low RMSE
- High prediction consistency

Notebook: `04_model_evaluation.ipynb`

---

## 5️⃣ Business Insights

- Identified key parameters affecting production
- Analyzed positive and negative feature impact
- Provided optimization suggestions

Notebook: `05_business_insights.ipynb`

---

# 📁 Project Structure

```
capstone-project1/
│
├── api/
│   ├── main.py              # FastAPI backend
│   └── schema.py            # Request/Response schema
│
├── models/
│   ├── linear_regression_model.pkl
│   └── scaler.pkl
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_model_training.ipynb
│   ├── 04_model_evaluation.ipynb
│   └── 05_business_insights.ipynb
│
├── app.py                   # Streamlit frontend
├── requirements.txt
└── README.md
```

---

# 🔌 FastAPI Backend

FastAPI is used to serve the trained Machine Learning model.

### API Endpoint
POST `/predict`

Input:
Machine operating parameters (JSON format)

Output:
Predicted production output (Parts_Per_Hour)

---

# 🖥️ Streamlit Frontend

Streamlit provides an interactive interface where users can:

- Enter machine parameters
- Click Predict
- View predicted output instantly

---

# 🧪 Example Input

```json
{
  "Injection_Temperature": 220,
  "Injection_Pressure": 85,
  "Cycle_Time": 55,
  "Cooling_Time": 20,
  "Material_Viscosity": 3.2,
  "Ambient_Temperature": 30,
  "Machine_Age": 5,
  "Operator_Experience": 4,
  "Maintenance_Hours": 120,
  "Machine_Utilization": 75,
  "Efficiency_Score": 80
}
```

---

# 🧪 Example Output

```json
{
  "parts_per_hour": 364.60
}
```

---

# 👥 Team Members & Responsibilities

## 🔹 Yashwanth (Group Leader)
- Model Training
- Model Evaluation
- Model Validation
- Business Insights
- Project Coordination

## 🔹 Anurag
- FastAPI Backend Development
- Model Integration with API
- Endpoint Creation

## 🔹 Lakshmi
- Data Exploration
- Data Preprocessing
- Streamlit Frontend Development

---

# 🧰 Technologies Used

Programming Language:
- Python

Libraries:
- Pandas
- NumPy
- Scikit-learn
- Joblib

Backend:
- FastAPI

Frontend:
- Streamlit

Tools:
- Jupyter Notebook

---

# ▶️ How to Run Locally

## Step 1: Create Virtual Environment
```
python -m venv env
```

Activate:
```
env\Scripts\activate
```

---

## Step 2: Install Dependencies
```
pip install -r requirements.txt
```

---

## Step 3: Run FastAPI Backend
```
uvicorn api.main:app --reload
```

---

## Step 4: Run Streamlit Frontend
```
streamlit run app.py
```

---

# 🎓 Learning Outcomes

Through this project, we gained experience in:

- End-to-end Machine Learning pipeline
- Data preprocessing techniques
- Regression modeling
- Model evaluation and validation
- Backend API development
- Frontend UI development
- Integrating ML models with web applications

---

# 📌 Conclusion

This project successfully demonstrates how Machine Learning can be integrated with backend and frontend technologies to build a real-world manufacturing prediction system.

The system predicts production output efficiently and supports data-driven decision making in industrial environments.
