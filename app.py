
import streamlit as st
from email_generator import generate_email


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Email Generator",
    page_icon="✉️",
    layout="centered"
)


# -----------------------------
# App Title
# -----------------------------
st.title("✉️ AI Email Generator")

st.write(
    "Generate professional emails instantly using AI."
)


# -----------------------------
# User Inputs
# -----------------------------

recipient = st.text_input(
    "Recipient",
    placeholder="e.g. Hiring Manager"
)


email_type = st.selectbox(
    "Email Type",
    [
        "Job Application",
        "Internship Application",
        "Follow-up",
        "Professional Request",
        "Thank You",
        "Meeting Request",
        "Complaint",
        "General Professional Email"
    ]
)


purpose = st.text_area(
    "What is the purpose of the email?",
    placeholder="e.g. I want to apply for an AI Engineer internship."
)


tone = st.selectbox(
    "Tone",
    [
        "Professional",
        "Formal",
        "Friendly",
        "Confident",
        "Concise"
    ]
)


length = st.selectbox(
    "Email Length",
    [
        "Short",
        "Medium",
        "Detailed"
    ]
)


additional_info = st.text_area(
    "Additional Information",
    placeholder="Add relevant skills, experience, dates, etc."
)


# -----------------------------
# Generate Email
# -----------------------------

if st.button("✨ Generate Email", use_container_width=True):

    if not purpose.strip():

        st.warning("Please enter the purpose of the email.")

    else:

        with st.spinner("Generating your email..."):

            try:

                # Get API key from Streamlit Secrets
                api_key = st.secrets["GROQ_API_KEY"]

                # Generate email
                email = generate_email(
                    api_key=api_key,
                    recipient=recipient,
                    purpose=purpose,
                    email_type=email_type,
                    tone=tone,
                    length=length,
                    additional_info=additional_info
                )

                st.success("Email generated successfully!")

                st.text_area(
                    "Generated Email",
                    value=email,
                    height=400
                )

            except Exception as e:

                st.error(f"Something went wrong: {str(e)}")
