import streamlit as st
import smtplib
from email.message import EmailMessage

st.set_page_config(page_title="Contact Me", layout="centered")

st.title("✉️ Send Me a Message")

with st.form("contact_form", clear_on_submit=True):
    name = st.text_input("Name*")
    email = st.text_input("Email*")
    subject = st.text_input("Subject*")
    message = st.text_area("Message*")
    
    submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        if name and email and message:
            # Note: You need a real email server (like Gmail/Outlook) to send this
            # This is a placeholder for your logic
            st.success("Message sent! (Note: Configure SMTP settings to receive emails)")
            # st.write(f"Sending email from {email}...")
        else:
            st.error("Please fill in all required fields.")