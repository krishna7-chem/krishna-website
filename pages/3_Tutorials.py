import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

st.set_page_config(page_title="CV | Krishna Karki", layout="wide")
st.header("📄 Curriculum Vitae")

with open("CV.pdf", "rb") as f:
    st.download_button("📥 Download CV (PDF)", f, file_name="Krishna_Karki_CV.pdf")

pdf_viewer("CV.pdf")