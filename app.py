import streamlit as st
import requests
import pandas as pd


API_URL = "https://matteoald-my-fastapi-endpoint.hf.space/predict"

st.title("Taxi Fare Prediction UI")

vendor_id = st.text_input("Vendor ID", value="Bogotá UberX")
dist_meters = st.number_input("Distance (m)", value=18.976)
wait_sec = st.number_input("Wait time (sec)", value=1640)
geodetic_dist = st.number_input("Geodetic Distance", value=15.439039)
mean_velocity = st.number_input("Mean Velocity", value=17.172851)
is_rush_hour = st.checkbox("Is Rush Hour?", value=False)
model_name = st.selectbox("Model Name", ["bog", "mex", "uio"], index=0)

if st.button("Predict"):
    data = {
        "vendor_id": vendor_id,
        "dist_meters": dist_meters,
        "wait_sec": wait_sec,
        "geodetic_dist": geodetic_dist,
        "mean_velocity": mean_velocity,
        "is_rush_hour": is_rush_hour,
        "model_name": model_name,
    }
    response = requests.post(API_URL, json=data, verify=False)
    if response.ok:
        st.json(response.json())
    else:
        st.error(f"Error: {response.text}")

st.header("Batch Prediction from CSV")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
model_name_csv = st.selectbox("Model Name for CSV", ["bog", "mex", "uio"], index=0)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("CSV Preview:", df.head())

    if st.button("Predict for CSV"):
        results = []
        for idx, row in df.iterrows():
            data = {
                "vendor_id": row["vendor_id"],
                "dist_meters": row["dist_meters"],
                "wait_sec": row["wait_sec"],
                "geodetic_dist": row["geodetic_dist"],
                "mean_velocity": row["mean_velocity"],
                "is_rush_hour": bool(row["is_rush_hour"]),
                "model_name": model_name_csv,  # Use selected model name for all rows
            }
            response = requests.post(API_URL, json=data, verify=False)
            if response.ok:
                result = response.json()
                result["row"] = idx
                results.append(result)
            else:
                results.append({"row": idx, "error": response.text})

        st.write("Batch Prediction Results:")
        st.write(pd.DataFrame(results))
