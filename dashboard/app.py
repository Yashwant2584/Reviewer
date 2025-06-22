"""
Streamlit dashboard for ReviewPulse.
"""
import streamlit as st
import requests
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

API_URL = os.getenv("REVIEWPULSE_API_URL", "http://localhost:8000/insights/summary")

st.set_page_config(page_title="ReviewPulse Dashboard", layout="wide")
st.title("ReviewPulse: Product Sentiment Insights")

product = st.text_input("Enter a product name:")

if product:
    with st.spinner("Fetching and analyzing reviews..."):
        try:
            response = requests.get(API_URL, params={"product": product})
            data = response.json()
        except Exception as e:
            st.error(f"API error: {e}")
            st.stop()

    if 'error' in data:
        st.error(f"Error: {data['error']}")
    else:
        st.subheader(f"Sentiment Distribution for '{product}'")
        counts = data.get('counts', {})
        total = data.get('total', 0)
        st.write(f"Total reviews/comments analyzed: {total}")
        # Bar chart
        fig = px.bar(x=list(counts.keys()), y=list(counts.values()), labels={'x': 'Sentiment', 'y': 'Count'}, title="Sentiment Counts")
        st.plotly_chart(fig, use_container_width=True)

        # Line chart (trend over sources)
        st.subheader("Sentiment by Source")
        sources = data.get('sources', {})
        source_counts = {src: len(sources[src].get('reviews', sources[src].get('comments', []))) for src in sources}
        fig2 = px.bar(x=list(source_counts.keys()), y=list(source_counts.values()), labels={'x': 'Source', 'y': 'Count'}, title="Mentions by Source")
        st.plotly_chart(fig2, use_container_width=True)

        # Word cloud
        st.subheader("Keyword Cloud")
        all_text = " ".join([s['text'] for s in data.get('all_sentiments', [])])
        if all_text:
            wordcloud = WordCloud(width=800, height=300, background_color='white').generate(all_text)
            fig_wc, ax = plt.subplots(figsize=(10, 3))
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis('off')
            st.pyplot(fig_wc)
        else:
            st.info("Not enough text for word cloud.")

        # Top reviews
        st.subheader("Top Positive Reviews")
        for r in data.get('top_positive', []):
            st.success(f"{r['text']}\n(Score: {r['score']:.2f})")
        st.subheader("Top Negative Reviews")
        for r in data.get('top_negative', []):
            st.error(f"{r['text']}\n(Score: {r['score']:.2f})")

        # Raw data expander
        with st.expander("Show raw data"):
            st.json(data)
else:
    st.info("Enter a product name to see sentiment insights.")
