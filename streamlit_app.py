import streamlit as st
import requests
from datetime import datetime

# Config
API_URL = "https://semantic-text-similarity-api-pvbh.onrender.com/similarity"
st.set_page_config(page_title="Text Similarity Tool", layout="wide")

# UI
st.title("🔍 Semantic Text Similarity")
col1, col2 = st.columns(2)
with col1:
    text1 = st.text_area("Text 1", "The cat sits on the mat")
with col2:
    text2 = st.text_area("Text 2", "A kitten rests on a rug")

# API Call
if st.button("Compare Texts", type="primary"):
    with st.spinner("Calculating..."):
        try:
            start_time = datetime.now()
            response = requests.post(
                API_URL,
                json={"text1": text1, "text2": text2},
                timeout=30  # Handle Render cold starts
            )
            processing_time = (datetime.now() - start_time).total_seconds()
            
            if response.status_code == 200:
                score = response.json()["similarity score"]
                st.success(f"**Similarity Score:** `{score:.4f}`")
                st.caption(f"Processed in {processing_time:.2f} seconds (including cold start)")
            else:
                st.error(f"API Error {response.status_code}: {response.text}")
                
        except Exception as e:
            st.error(f"Failed to connect to API. Please try again.\nError: {str(e)}")