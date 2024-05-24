import PyPDF2
from langchain import LangChain

def extract_text_from_pdf(pdf_content: bytes) -> str:
    reader = PyPDF2.PdfFileReader(pdf_content)
    text = ""
    for page_num in range(reader.getNumPages()):
        text += reader.getPage(page_num).extract_text()
    return text

def answer_question(document_content: str, question: str) -> str:
    llm = LangChain(model_name="gpt-3")
    response = llm.run(document_content, question)
    return response
