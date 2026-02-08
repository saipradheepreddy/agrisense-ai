import streamlit as st
import pandas as pd

st.set_page_config(page_title="AgriSense AI", layout="centered")

st.title("🌱 AgriSense AI")
st.subheader("End-to-End Smart Farming Decision System")

st.markdown("""
This system helps farmers decide:
- **What to grow**
- **How risky it is**
- **When to sell**
- **How to farm sustainably**
""")

st.divider()
st.header("🌾 Step 1: Crop Suitability & Risk")

crop_data = pd.read_csv("crop_suitability_data.csv")

location = st.selectbox("📍 Location", crop_data["Location"].unique())
season = st.selectbox("🌦 Season", ["Kharif", "Rabi", "Summer"])
rainfall = st.selectbox("🌧 Rainfall", ["Low", "Medium", "High"])
temperature = st.selectbox("🌡 Temperature", ["Low", "Medium", "High"])
def score(val):
    return {"High": 2, "Medium": 1, "Low": 0}.get(val, 0)
if st.button("🔍 Analyze Crop"):
    filtered = crop_data[
        (crop_data["Location"] == location) &
        (crop_data["Season"] == season) &
        (crop_data["Rainfall"] == rainfall) &
        (crop_data["Temperature"] == temperature)
    ]

    if filtered.empty:
        st.warning("Exact match not found. Showing closest crops.")
        filtered = crop_data[
            (crop_data["Location"] == location) &
            (crop_data["Season"] == season)
        ]

    st.subheader("✅ Recommended Crops")

    for _, row in filtered.iterrows():
        total = score(row["Past_Success"]) + score(row["Water_Availability"]) + score(row["Adoption"])

        if total >= 5:
            risk = "🟢 Low"
        elif total >= 3:
            risk = "🟡 Medium"
        else:
            risk = "🔴 High"

        st.write(f"🌱 **{row['Crop']}** — Risk Level: {risk}")
st.divider()
st.header("📈 Step 2: Price Trend & Selling Advice")

price_data = pd.read_csv("crop_price_data.csv")

selected_crop = st.selectbox("🌾 Select Crop for Price Analysis", price_data["Crop"].unique())

crop_prices = price_data[price_data["Crop"] == selected_crop]
prices = crop_prices["Avg_Price"].values

if prices[-1] > prices[0]:
    trend = "📈 Increasing → Better to WAIT"
elif prices[-1] < prices[0]:
    trend = "📉 Decreasing → Better to SELL now"
else:
    trend = "➖ Stable → Sell anytime"
if st.button("📊 Analyze Price Trend"):
    st.write(f"**Price Trend:** {trend}")
    st.write(f"**Expected Range:** ₹{prices.min()} – ₹{prices.max()} per quintal")
    st.line_chart(crop_prices.set_index("Month")["Avg_Price"])
st.divider()
st.header("♻️ Step 3: Sustainability Advice")

st.write("🌍 **General Sustainable Suggestions:**")

st.markdown("""
- Prefer crops with **low water requirement**
- Use **organic compost** where possible
- Rotate crops to maintain soil health
- Avoid over-irrigation
""")
python -m streamlit run app.py
