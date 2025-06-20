# 🧠 Taxi Fare Prediction GUI

This is a simple Gradio-based web application that allows users to interact with a machine learning model hosted on [Hugging Face Spaces](https://huggingface.co/spaces). The model predicts taxi fare data based on input features such as distance, wait time, and rush hour flag.

---

## 🚀 Features

✅ Manual input of a single data point  
✅ Upload multiple data points via `.csv` file  
✅ Scrollable table to view all predictions  
✅ Visualize predictions alongside input features  
✅ Delete individual datapoints with confirmation  
✅ Export results to a `.csv` file

---

## 🧩 App Structure

```bash
.
├── app.py         # Gradio frontend application
├── requirements.txt
└── README.md
```

## 🛠️ Installation

docker build -t taxi-fare-ui .
docker run -p 8501:8501 taxi-fare-ui
