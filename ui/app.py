import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="GitHub Code Mentor", page_icon="🐙")

st.title("🐙 The Student GitHub & Portfolio Reviewer")
username = st.text_input("GitHub Username:", placeholder="e.g., torvalds")

if st.button("Analyze Portfolio"):
    if username:
        with st.spinner(f"Analyzing {username}'s repositories..."):
            try:
                # Fetch backend URL from environment variables
                backend_url = os.getenv("BACKEND_URL", "http://127.0.0.1:8001/review")
                
                response = requests.post(
                    backend_url, 
                    json={"username": username}
                )
                
                if response.status_code == 200:
                    data = response.json()
                    st.success("Analysis Complete!")
                    st.json(data["extracted_data"])
                    st.write(data["mentor_feedback"])
                else:
                    st.error(f"Backend Error: {response.status_code}")
            except Exception as e:
                st.error("Could not connect to the backend.")

