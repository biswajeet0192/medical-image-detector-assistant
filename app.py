import streamlit as st
from pathlib import Path
import google.generativeai as genai

st.set_page_config(page_title = "VitalImage Analytics", page_icon = ":robot:")

st.image("skillcurb.png", width=150)

st.title("Vital Image Analytics")

st.subheader("An application that can help users to identify medical images")

uploaded_file = st.file_uploader("Upload an medical image for analysis", type = ['png', 'jpg', 'jpeg'])

submit_button = st.button("Generate the Analysis")

if submit_button:
    pass