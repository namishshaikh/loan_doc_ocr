import streamlit as st
from utils.ocr_utils import extract_text, extract_fields
from utils.validation import validate_data

st.title("Automated Personal Loan Document Processing")

uploaded_file = st.file_uploader("Upload Loan Document", type=["jpg", "jpeg", "png", "pdf"])
if uploaded_file:
    with open(f"temp_{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.read())
    
    text = extract_text(f"temp_{uploaded_file.name}")
    fields = extract_fields(text)
    validated = validate_data(fields)

    st.subheader("Extracted Data")
    st.json(fields)

    st.subheader("Validation Status")
    st.json(validated)