from src.mcqgenerator.logger import logging
from src.mcqgenerator.utils import read_file

logging.info("start my process")
filepath = r"C:\Users\Admin\MCQ_generator-Using-Langchain-and-OpenAI\data.txt"
TEXT = read_file(file_path=filepath)
print(TEXT)