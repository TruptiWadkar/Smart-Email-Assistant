# smart_ui.py

import streamlit as st
from orchestrator import process_email

st.set_page_config(page_title="Smart Email Assistant", layout="centered")

# Sidebar - Info
with st.sidebar:
    st.title("Smart Email Assistant")
    st.markdown("""
    This tool processes internal company emails by:
    - Classifying emails into HR, IT, or Other
    - Generating replies using Gemini AI
    - Escalating uncertain messages for review
    """)

# Main Title
st.title("Internal Email Handling Tool")
st.markdown("Paste an internal company email below. The system will respond or escalate based on analysis.")

# Input Form
st.subheader("Enter Email Content")
email_input = st.text_area("Email Body", height=180)

# Submit Button
if st.button("Submit") and email_input.strip():
    with st.spinner("Processing your email..."):
        result = process_email(email_input)

        st.markdown("---")

        if result["stage"] == "response_generated":
            st.success("AI Response Generated")
            st.write(f"Predicted Category: {result['category']}")
            st.write(f"Confidence Score: {result['confidence']}")

            # Show response in a copyable, editable textbox
            st.subheader("Generated Reply")
            st.text_area("AI-Generated Email Reply", value=result["response"], height=180)

        elif result["stage"] == "escalated":
            st.warning("Email Escalated for Manual Review")
            st.write(f"Reason: {result['reason']}")
            st.write(f"Predicted Category: {result['category']}")
            st.write(f"Confidence Score: {result['confidence']}")
            st.write(f"Logged to: {result['logged_to']}")
else:
    st.caption("Enter a valid email and press Submit.")
