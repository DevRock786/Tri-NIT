# from fastapi import FastAPI, UploadFile, File, HTTPException
# import requests
# import re

# app = FastAPI()

# # Function to perform OCR on the uploaded image
# def ocr_space_file(filename, api_key, language='eng'):
#     try:
#         payload = {'apikey': api_key,
#                    'language': language,
#                    'isOverlayRequired': False}
#         with open(filename, 'rb') as f:
#             r = requests.post('https://api.ocr.space/parse/image',
#                               files={filename: f},
#                               data=payload)
#         r.raise_for_status()  # Raise HTTPError if request was unsuccessful
#         return r.json()
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"OCR processing failed: {e}")

# # Endpoint to upload an image for OCR processing
# @app.post("/upload/")
# async def upload_image(file: UploadFile = File(...)):
#     try:
#         # Save the uploaded file
#         with open(file.filename, "wb") as buffer:
#             buffer.write(await file.read())

#         # Perform OCR on the uploaded image
#         api_key = 'K82475335888957'  # Replace with your OCR.space API key
#         result_json = ocr_space_file(file.filename, api_key)
        
#         # Return the OCR result
#         return result_json
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error processing image: {e}")

# # Endpoint to search for specific keywords in the extracted text
# @app.get("/search/")
# async def search_text(keyword: str):
#     try:
#         # Perform search functionality on the extracted text
#         # Example implementation: return matching sections of the text containing the keyword
#         extracted_text = """
#         3.
#         4.
#         How many different signals can be given using any number of flags from 5 flags of different colors (that is, all the flags are distinct)
#         (1) 350
#         (2) 351
#         (3) 325
#         (4) 326
#         Find the number Of permutations Of all the letters Of the word MATHEMATICS which Starts with consonants only. Given 10! k;
#         (1) 7k/8
#         (2) 2k/3
#         (3) 6k/7
#         """
#         # Example implementation: Parse the text and return sections containing the keyword
#         matching_sections = [section.strip() for section in extracted_text.split('\n') if keyword in section]
#         return {"matching_sections": matching_sections}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error searching text: {e}")

# # Endpoint to provide quiz questions and options
# import re

# # Endpoint to provide quiz questions and options
# @app.get("/quiz/")
# async def get_quiz():
#     try:
#         # Extracted text containing quiz questions and options
#         extracted_text = """
#         3.
#         How many different signals can be given using any number of flags from 5 flags of different colors (that is, all the flags are distinct)
#         (1) 350
#         (2) 351
#         (3) 325
#         (4) 326
#         4.
#         Find the number Of permutations Of all the letters Of the word MATHEMATICS which Starts with consonants only. Given 10! k;
#         (1) 7k/8
#         (2) 2k/3
#         (3) 6k/7
#         """
#         # Split the extracted text into lines
#         lines = [line.strip() for line in extracted_text.split("\n") if line.strip()]

#         # Construct quiz data
#         quiz_data = {}
#         current_question = None
#         for line in lines:
#             if line.endswith("."):
#                 current_question = line
#                 quiz_data[current_question] = []
#             else:
#                 quiz_data[current_question].append(line)

#         return {"quiz": quiz_data}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error retrieving quiz: {e}")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)


# from fastapi import FastAPI, UploadFile, File, HTTPException
# import magic # for file type detection
# app = FastAPI()

# # Function to perform OCR on the uploaded image
# def ocr_space_file(filename, api_key, language='eng'):
#     # Perform OCR processing here
#     pass

# def ocr_pdf_file(pdf_content):
#     # Placeholder functionality for PDF OCR processing
#     # Replace this with actual PDF OCR processing logic
#     pass

# # Function to process the OCR result and extract questions and options dynamically
# def process_ocr_result(result_json):
#     # Parse the OCR result and extract questions and options
#     # This function will vary depending on the structure of the OCR result
#     pass

# # Sample extracted text
# extracted_text = """
# Text extracted from OCR processing.
# Contains multiple lines.
# Each line may contain relevant information.
# """

# # Sample dictionary to store questions and options
# questions_data = {
#     "Question 1": ["Option 1", "Option 2", "Option 3", "Option 4"],
#     "Question 2": ["Option 1", "Option 2", "Option 3", "Option 4"]
# }

# # Endpoint to upload an image for OCR processing
# async def upload_pdf(file: UploadFile = File(...)):
#     # Check if the uploaded file is a PDF
#     mime_type = magic.Magic(mime=True)
#     file_type = mime_type.from_buffer(await file.read(1024))
#     if file_type != "application/pdf":
#         raise HTTPException(status_code=400, detail="Uploaded file must be a PDF")

#     # Perform OCR on the PDF file
#     ocr_result = ocr_pdf_file(await file.read())

#     # Process the OCR result to extract questions
#     questions = process_ocr_result(ocr_result)

#     # Return the extracted questions
#     return {"questions": questions}

# # async def upload_image(file: UploadFile = File(...)):
# #     # Save the uploaded file
# #     with open(file.filename, "wb") as buffer:
# #         buffer.write(await file.read())

# #     # Perform OCR on the uploaded image
# #     api_key = 'K82475335888957'  # Replace with your OCR.space API key
# #     result_json = ocr_space_file(file.filename, api_key)
    
# #     # Process the OCR result to extract questions and options dynamically
# #     extracted_questions = process_ocr_result(result_json)

# #     # Return the extracted questions and options
# #     return {"questions": extracted_questions}

# # Endpoint to answer a question
# @app.get("/answer/")
# async def answer_question(question: str):
#     if question in questions_data:
#         return {"question": question, "options": questions_data[question]}
#     else:
#         raise HTTPException(status_code=404, detail="Question not found")

# # Endpoint to search for specific keywords
# @app.get("/search/")
# async def search_text(keyword: str):
#     # Logic to search for keyword in the extracted text
#     matching_sections = [section.strip() for section in extracted_text.split('\n') if keyword in section]
#     return {"keyword": keyword, "matching_sections": matching_sections}

# # Endpoint to retrieve the extracted text
# @app.get("/text/")
# async def get_extracted_text():
#     return {"text": extracted_text}

# # Endpoint to add new questions and options
# @app.post("/add/")
# async def add_question(question: str, options: list):
#     if question not in questions_data:
#         questions_data[question] = options
#         return {"message": "Question added successfully"}
#     else:
#         raise HTTPException(status_code=400, detail="Question already exists")

# # Endpoint to edit existing questions and options
# @app.put("/edit/")
# async def edit_question(question: str, new_options: list):
#     if question in questions_data:
#         questions_data[question] = new_options
#         return {"message": "Question edited successfully"}
#     else:
#         raise HTTPException(status_code=404, detail="Question not found")

# # Endpoint to delete existing questions and options
# @app.delete("/delete/")
# async def delete_question(question: str):
#     if question in questions_data:
#         del questions_data[question]
#         return {"message": "Question deleted successfully"}
#     else:
#         raise HTTPException(status_code=404, detail="Question not found")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
    
# from fastapi import FastAPI, UploadFile, File, HTTPException
# import magic
# import io
# import pytesseract
# from pdf2image import convert_from_bytes
# from pdfplumber import PdfFileReader

# app = FastAPI()

# # Function to perform OCR on the uploaded image
# def ocr_space_file(filename, api_key, language='eng'):
#     pass 

# def ocr_pdf_file(pdf_content):
#     extracted_text = ""

#     # Create a PdfFileReader object
#     pdf_reader = PdfFileReader(io.BytesIO(pdf_content))

#     # Iterate through each page of the PDF and extract text
#     for page_num in range(pdf_reader.numPages):
#         page = pdf_reader.getPage(page_num)
#         extracted_text += page.extractText()

#     return extracted_text
# # Function to process the OCR result and extract questions and options dynamically
# def process_ocr_result(result_json):
#     parsed_results = result_json.get("ParsedResults", [])
#     extracted_questions = {}
    
#     for parsed_result in parsed_results:
#         parsed_text = parsed_result.get("ParsedText", "")
#         lines = parsed_text.split("\n")
        
#         current_question = None
#         options = []

#         for line in lines:
#             line = line.strip()
#             if line.endswith("?"):
#                 current_question = line
#                 options = []
#             elif line.startswith("(") and line.endswith(")"):
#                 options.append(line)
#             elif line:
#                 options.append(line)

#         if current_question and options:
#             extracted_questions[current_question] = options
    
#     return extracted_questions

# # Sample extracted text
# extracted_text = """
# Text extracted from OCR processing.
# Contains multiple lines.
# Each line may contain relevant information.
# """

# # Sample dictionary to store questions and options
# questions_data = {
#     "Question 1": ["Option 1", "Option 2", "Option 3", "Option 4"],
#     "Question 2": ["Option 1", "Option 2", "Option 3", "Option 4"]
# }

# async def upload_pdf(file: UploadFile = File(...)):
#     # Check if the uploaded file is a PDF
#     mime_type = magic.Magic(mime=True)
#     file_type = mime_type.from_buffer(await file.read(1024))
#     if file_type != "application/pdf":
#         raise HTTPException(status_code=400, detail="Uploaded file must be a PDF")

#     # Perform OCR on the PDF file
#     pdf_content = await file.read()
#     extracted_text = ocr_pdf_file(pdf_content)

#     # Return the extracted text
#     return {"extracted_text": extracted_text}

# # Endpoint to upload an image for OCR processing
# # @app.post("/upload/")
# # async def upload_image(file: UploadFile = File(...)):
# #     # Perform OCR on the uploaded image
# #     # Replace 'api_key' with your OCR.space API key
# #     api_key = 'K82475335888957'
# #     result_json = ocr_space_file(file.filename, api_key)
    
# #     # Process the OCR result to extract questions and options dynamically
# #     extracted_questions = process_ocr_result(result_json)

# #     # Return the extracted questions and options
# #     return {"questions": extracted_questions}

# # Endpoint to answer a question
# @app.get("/answer/")
# async def answer_question(question: str):
#     if question in questions_data:
#         return {"question": question, "options": questions_data[question]}
#     else:
#         raise HTTPException(status_code=404, detail="Question not found")

# # Endpoint to search for specific keywords
# @app.get("/search/")
# async def search_text(keyword: str):
#     # Logic to search for keyword in the extracted text
#     matching_sections = [section.strip() for section in extracted_text.split('\n') if keyword in section]
#     return {"keyword": keyword, "matching_sections": matching_sections}

# # Endpoint to retrieve the extracted text
# @app.get("/text/")
# async def get_extracted_text():
#     return {"text": extracted_text}

# # Endpoint to add new questions and options
# @app.post("/add/")
# async def add_question(question: str, options: list):
#     if question not in questions_data:
#         questions_data[question] = options
#         return {"message": "Question added successfully"}
#     else:
#         raise HTTPException(status_code=400, detail="Question already exists")

# # Endpoint to edit existing questions and options
# @app.put("/edit/")
# async def edit_question(question: str, new_options: list):
#     if question in questions_data:
#         questions_data[question] = new_options
#         return {"message": "Question edited successfully"}
#     else:
#         raise HTTPException(status_code=404, detail="Question not found")

# # Endpoint to delete existing questions and options
# @app.delete("/delete/")
# async def delete_question(question: str):
#     if question in questions_data:
#         del questions_data[question]
#         return {"message": "Question deleted successfully"}
#     else:
#         raise HTTPException(status_code=404, detail="Question not found")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)


from fastapi import FastAPI, UploadFile, File, HTTPException
import magic
import io
from pdfplumber import PdfFileReader

app = FastAPI()

# Function to perform OCR on the uploaded image
def ocr_space_file(filename, api_key, language='eng'):
    pass 

def ocr_pdf_file(pdf_content):
    extracted_text = ""

    # Create a PdfFileReader object
    pdf_reader = PdfFileReader(io.BytesIO(pdf_content))

    # Iterate through each page of the PDF and extract text
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        extracted_text += page.extractText()

    return extracted_text

# Function to process the OCR result and extract questions and options dynamically
def process_ocr_result(result_json):
    pass

# Sample extracted text
extracted_text = """
Text extracted from OCR processing.
Contains multiple lines.
Each line may contain relevant information.
"""

# Sample dictionary to store questions and options
questions_data = {
    "Question 1": ["Option 1", "Option 2", "Option 3", "Option 4"],
    "Question 2": ["Option 1", "Option 2", "Option 3", "Option 4"]
}

# Endpoint to upload a PDF file for OCR processing
@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    pass

# Endpoint to answer a question
@app.get("/answer/")
async def answer_question(question: str):
    pass

# Endpoint to search for specific keywords
@app.get("/search/")
async def search_text(keyword: str):
    pass

# Endpoint to retrieve the extracted text
@app.get("/text/")
async def get_extracted_text():
    pass

# Endpoint to add new questions and options
@app.post("/add/")
async def add_question(question: str, options: list):
    pass

# Endpoint to edit existing questions and options
@app.put("/edit/")
async def edit_question(question: str, new_options: list):
    pass

# Endpoint to delete existing questions and options
@app.delete("/delete/")
async def delete_question(question: str):
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
