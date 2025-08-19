import os
import google.generativeai as genai
from  PyPDF2 import PdfReader

genai.configure(api_key="")


model = genai.GenerativeModel("gemini-1.5-flash")   

def medical_Assistant(details,pdf):
        def pdf_text(file):
            reader = PdfReader(file)  # This should now work correctly
            text = ""
            for page in reader.pages:  # Iterate through the pages
                text += page.extract_text()  # Extract text from each page
            return text
        pdf_content = pdf_text(pdf)
        input_prompt_template = f""""""
        res = model.generate_content([pdf_content, input_prompt_template])
        return res.text
