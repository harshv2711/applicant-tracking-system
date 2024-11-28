import PyPDF2

def convertPdfToText(fileObject):
    # Create a PdfReader object instead of PdfFileReader
    pdf_reader = PyPDF2.PdfReader(fileObject)
    # Initialize an empty string to store the text
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    return text
