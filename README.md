 # 💳 Credit Card Fraud Detection App

An interactive web app that detects fraudulent transactions using a machine learning model trained on synthetic data. Built with **Streamlit** and deployed on **Hugging Face Spaces**.

![Streamlit App Screenshot](https://github.com/user-attachments/assets/ee4f9c9a-adfd-4726-b7df-81d14b03bfe2)
![image](https://github.com/user-attachments/assets/6f4f14f3-8d9a-44b4-b464-559fdfd9a44c)


## 🚀 Features

- 📊 Input 29 transaction-related features manually
- ⚙️ Predict fraud probability using a trained `RandomForestClassifier`
- 🌐 Deployed with Hugging Face Spaces
- 🧠 Model built with `scikit-learn` on synthetic tabular data

## 🔗 Live Demo

👉 [Launch the App on Hugging Face Spaces](https://mukil-kumar-v-credit-card-fraud-detection.hf.space/#credit-card-fraud-detection)


## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **Scikit-learn**
- **Hugging Face Spaces**


## 📁 Project Structure
```
credit-card-fraud-app/
├── app.py # Streamlit UI
├── rf_model.pkl # Trained ML model (RandomForest)
├── requirements.txt # Dependencies
└── README.md # Project Overview
```

## 📦 Setup Instructions (Local)
```
git clone https://github.com/Mukilkumar-SEC/credit-card-fraud-app.git
cd credit-card-fraud-app
pip install -r requirements.txt
streamlit run app.py
```
## 🤖 Model Training 
```python

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import pickle

X, y = make_classification(n_samples=1000, n_features=29, random_state=42)
model = RandomForestClassifier()
model.fit(X, y)

with open("rf_model.pkl", "wb") as f:
    pickle.dump(model, f)
```
## 📄 License
This project is licensed under the MIT License.
