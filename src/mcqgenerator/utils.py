import os
import json
import PyPDF2
import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader= PyPDF2.PdfFileReader(file)
            text=""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text
        except Exception as e:
            raise Exception("File not found")
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    else:
        raise Exception("Unsupposrted file format only pdf and txt format supported")
    
def get_table_data(quiz):
    try:
        quiz_table_data = []
        quiz= json.loads(quiz)
        for key, value in quiz.items():
            mcq = value["mcq"]
            options = " | ".join(
                [
                    f"{option}: {option_value}"
                    for option, option_value in value["options"].items()
                    ]
                )
            correct = value["correct"]
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})
            return quiz_table_data
        
    except:
        raise Exception("No mcq available")

