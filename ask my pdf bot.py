from google import genai
import PyPDF2

client = genai.Client(api_key="AIzaSyBskgQmaaciYLjWDvlkHg9_iBYpg0bWDLU")

with open("review 1 GL.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)

    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

question = input("Ask question from PDF: ")

prompt = f"""
Use the PDF text to answer. If exact answer is not found, give a simple general answer also.

PDF text:
{text}

Question:
{question}
"""

response = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview",
    contents=prompt
)

print(response.text)