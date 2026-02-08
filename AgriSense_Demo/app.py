import streamlit as st
import pandas as pd

st.set_page_config(page_title="AgriSense AI", layout="centered")

st.title("🌱 AgriSense AI")
st.subheader("Climate-Resilient Crop Recommendation System")
st.markdown(
    "Helping farmers choose **safe and sustainable crops** "
    "based on climate and historical success."
)

# Load dataset
data = pd.read_csv("crop_suitability_data.csv")

st.divider()

# -------- USER INPUTS --------
location = st.selectbox("📍 Select Location", sorted(data["Location"].unique()))
season = st.selectbox("🌦️ Select Season", ["Kharif", "Rabi", "Summer"])
rainfall = st.selectbox("🌧️ Rainfall Level", ["Low", "Medium", "High"])
temperature = st.selectbox("🌡️ Temperature Level", ["Low", "Medium", "High"])

st.divider()

# -------- ANALYZE BUTTON --------
def score(val):
    return {"High": 2, "Medium": 1, "Low": 0}.get(val, 0)

if st.button("🔍 Analyze Crop Suitability"):
    filtered = data[
        (data["Location"] == location) &
        (data["Season"] == season) &
        (data["Rainfall"] == rainfall) &
        (data["Temperature"] == temperature)
    ]

    if filtered.empty:
        st.warning("⚠️ Exact match not found. Showing closest suitable crops.")
        filtered = data[
            (data["Location"] == location) &
            (data["Season"] == season)
        ]

    st.success("✅ Analysis Completed")
    st.subheader("🌾 Crop Suitability Results")

    for _, row in filtered.iterrows():
        total = (
            score(row["Past_Success"]) +
            score(row["Water_Availability"]) +
            score(row["Adoption"])
        )

        if total >= 5:
            risk = "🟢 Low"
            color = "#e8f5e9"
        elif total >= 3:
            risk = "🟡 Medium"
            color = "#fffde7"
        else:
            risk = "🔴 High"
            color = "#ffebee"

        st.markdown(
            f"""
            <div style="background-color:{color}; padding:16px; border-radius:12px;">
            <h4>🌱 {row['Crop']}</h4>
            <b>Risk Level:</b> {risk}<br>
            <small>
            Past Success: {row['Past_Success']} | 
            Water: {row['Water_Availability']} | 
            Adoption: {row['Adoption']}
            </small>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.write("")

