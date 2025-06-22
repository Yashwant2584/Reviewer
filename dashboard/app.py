"""
Streamlit dashboard for ReviewPulse.
"""
import streamlit as st

st.set_page_config(page_title="ReviewPulse Dashboard", layout="wide")
st.title("ReviewPulse: Product Sentiment Insights")

product = st.text_input("Enter a product name:")

if product:
    st.write(f"Showing insights for: {product}")
    # Placeholder for charts and insights
    st.info("Visualizations and insights will appear here.")
