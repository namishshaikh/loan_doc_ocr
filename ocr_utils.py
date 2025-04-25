import easyocr
import re
reader = easyocr.Reader(['en'])

def extract_text(image_path):
    result = reader.readtext(image_path, detail=0)
    return " ".join(result)

def extract_fields(text):
    fields = {}

    # Example regex patterns – these should be tailored to your actual document format
    name_match = re.search(r"Name\s*[:\-]?\s*([A-Za-z ]+)", text, re.IGNORECASE)
    address_match = re.search(r"Address\s*[:\-]?\s*(.+?)(?:Income|Loan Amount|$)", text, re.IGNORECASE | re.DOTALL)
    income_match = re.search(r"Income\s*[:\-]?\s*([\d,]+)", text, re.IGNORECASE)
    loan_amount_match = re.search(r"Loan Amount\s*[:\-]?\s*([\d,]+)", text, re.IGNORECASE)

    fields["Name"] = name_match.group(1).strip() if name_match else ""
    fields["Address"] = address_match.group(1).strip().replace("\\n", " ") if address_match else ""
    fields["Income"] = income_match.group(1).strip() if income_match else ""
    fields["Loan Amount"] = loan_amount_match.group(1).strip() if loan_amount_match else ""

    return fields