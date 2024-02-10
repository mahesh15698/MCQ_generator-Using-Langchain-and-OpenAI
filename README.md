# MCQ Project Generator
This is a Python-based application for generating multiple-choice quizzes using OpenAI's GPT-3.5 language model, Langchain Framework and Streamlit for the user interface.
# Features

#### Generate multiple-choice quizzes from text files or PDFs.

#### Specify the number of questions, subject, and complexity level of the quizzes.

#### Evaluate the complexity of generated quizzes and update them if needed.

#### Easily accessible through a user-friendly web interface created with Streamlit.

## Installation

### 1. Clone this repository to your local machine
```
https://github.com/mahesh15698/MCQ_generator_Using_Langchain_and_OpenAI.git

```
### 2. Create New Environment 
```
Conda create -p [env_name] python==[version] -y
```

### 3. Install the required dependencies using pip
```
pip install -r requirements.txt
```
### 4.Set up environment variables:

##### Create a .env file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key
```
### 5.Usage
##### Run the Streamlit application:

```
streamlit run app.py

```

### Access the application in your web browser at the provided URL.

### Upload a PDF or text file containing the text you want to generate quizzes from.

### Enter the number of MCQs, subject, and complexity level, then click "Create MCQs".

### View the generated quiz and its evaluation.


# Acknowledgements
#### This project uses OpenAI's GPT-3.5 language model for text generation.
#### Streamlit is used for building the user interface.

# Contact
#### For questions or inquiries, please contact maheshjadhav7979@gmail.com.
