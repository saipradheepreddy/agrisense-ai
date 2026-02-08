# 🌱 AgriSense AI  
### Climate-Resilient Crop Recommendation System

AgriSense AI is a decision-support web application that helps farmers choose
**safe and sustainable crops** based on climate conditions and historical data.

---

## 🚩 Problem Statement
Due to climate change, farmers often face:
- Unpredictable rainfall and temperature
- Crop failure due to poor crop selection
- Water and resource wastage

Most crop decisions are made based on tradition rather than data.

---

## 💡 Our Solution
AgriSense AI analyzes:
- Location
- Season
- Rainfall level
- Temperature level

and combines them with:
- Historical crop success
- Water availability
- Farmer adoption patterns

to recommend crops with a **clear risk level**.

---

## ⚙️ Features
- 🌾 Climate-based crop recommendation
- ⚠️ Risk levels (Low / Medium / High)
- 🧠 Explainable AI logic
- 🌍 Sustainability-focused decision making
- 💻 Web-based interface (Streamlit)

---

## 🧠 Risk Calculation Logic
Each crop is scored using:
- Past Success
- Water Availability
- Farmer Adoption

Scoring:
- High = 2
- Medium = 1
- Low = 0

Final Risk:
- 5–6 → Low Risk
- 3–4 → Medium Risk
- 0–2 → High Risk

This keeps the system **transparent and explainable**.

---

## 🖥️ Tech Stack
- Python
- Streamlit
- Pandas
- CSV-based dataset

---

## 🚀 How to Run Locally
```bash
pip install -r requirements.txt
python -m streamlit run app.py
