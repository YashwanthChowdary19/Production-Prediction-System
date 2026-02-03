import streamlit as st
import requests
import json

# MUST be the first Streamlit command
st.set_page_config(
    page_title="Manufacturing Output Predictor",
    layout="wide"
)

st.title("🏭 Manufacturing Equipment Output Predictor")
st.markdown("Predict **Parts Per Hour** using machine operating parameters")

API_URL = "http://127.0.0.1:8000/predict"

# -----------------------------
# Input Form
# -----------------------------
with st.form("prediction_form"):
    st.subheader("🔧 Machine Parameters")

    col1, col2, col3 = st.columns(3)

    with col1:
        injection_temperature = st.number_input("Injection Temperature", 150.0, 350.0, 250.0)
        injection_pressure = st.number_input("Injection Pressure", 50.0, 300.0, 150.0)
        cycle_time = st.number_input("Cycle Time", 5.0, 120.0, 30.0)
        cooling_time = st.number_input("Cooling Time", 5.0, 120.0, 20.0)
        material_viscosity = st.number_input("Material Viscosity", 1.0, 10.0, 5.0)

    with col2:
        ambient_temperature = st.number_input("Ambient Temperature", 10.0, 50.0, 25.0)
        machine_age = st.number_input("Machine Age (years)", 0.0, 20.0, 5.0)
        operator_experience = st.number_input("Operator Experience (years)", 0.0, 20.0, 5.0)
        maintenance_hours = st.number_input("Maintenance Hours", 0.0, 200.0, 20.0)
        machine_utilization = st.number_input("Machine Utilization (%)", 0.0, 100.0, 80.0)

    with col3:
        shift = st.selectbox("Shift", ["Day", "Evening", "Night"])
        machine_type = st.selectbox("Machine Type", ["Type_A", "Type_B", "Type_C"])
        material_grade = st.selectbox("Material Grade", ["Economy", "Standard", "Premium"])
        day_of_week = st.selectbox(
            "Day of Week",
            ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        )
        efficiency_score = st.number_input("Efficiency Score", 0.0, 100.0, 85.0)

    submit = st.form_submit_button("🚀 Predict Output")

# -----------------------------
# Prediction Logic
# -----------------------------
if submit:
    temperature_pressure_ratio = injection_temperature / injection_pressure
    total_cycle_time = cycle_time + cooling_time

    payload = {
        "Injection_Temperature": injection_temperature,
        "Injection_Pressure": injection_pressure,
        "Cycle_Time": cycle_time,
        "Cooling_Time": cooling_time,
        "Material_Viscosity": material_viscosity,
        "Ambient_Temperature": ambient_temperature,
        "Machine_Age": machine_age,
        "Operator_Experience": operator_experience,
        "Maintenance_Hours": maintenance_hours,
        "Shift": shift,
        "Machine_Type": machine_type,
        "Material_Grade": material_grade,
        "Day_of_Week": day_of_week,
        "Efficiency_Score": efficiency_score,
        "Machine_Utilization": machine_utilization,
        "Temperature_Pressure_Ratio": temperature_pressure_ratio,
        "Total_Cycle_Time": total_cycle_time
    }


    try:
        response = requests.post(
            API_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload),
            timeout=10
        )

        if response.status_code == 200:
            result = response.json()
            st.success("✅ Prediction Successful!")
            st.metric(
                label="📦 Predicted Parts Per Hour",
                value=f"{result['parts_per_hour']:.2f}"
            )
        else:
            st.error(f"❌ API Error ({response.status_code})")
            st.code(response.text)

    except Exception as e:
        st.error("❌ Error connecting to prediction API")
        st.exception(e)
