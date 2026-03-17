import streamlit as st
from utils import extract_skills, retrieve_portfolio_links, generate_email

st.set_page_config(page_title="Cold Email Generator", page_icon="📧")
st.title("Cold Email Generator")

job_description = st.text_area("Paste Job Description", height=250)

if st.button("Generate Email"):
    if not job_description.strip():
        st.warning("Please paste a job description.")
    else:
        skills = extract_skills(job_description)
        links = retrieve_portfolio_links(skills)
        email = generate_email(job_description, skills, links)

        st.subheader("Extracted Skills")
        st.write(skills)

        st.subheader("Relevant Portfolio Links")
        for link in links:
            st.write(f"- {link}")

        st.subheader("Generated Email")
        st.code(email, language="text")
