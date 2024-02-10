# MCQ Project Generator
This is a Python-based application for generating multiple-choice quizzes using OpenAI's GPT-3.5 language model, Langchain Framework and Streamlit for the user interface.

# User Interface on Streamlit
![Interface](https://github.com/mahesh15698/MCQ_generator_Using_Langchain_and_OpenAI/blob/main/experiment/mqsoutput.PNG)
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
### 5.Set up environment variables:
```
Setup langchain chain use document
```
### 6.Usage
##### Run the Streamlit application:

```
streamlit run app.py

```
## AWS Deployement Setup

### 1. [First login to the AWS](https://aws.amazon.com/console/)

### 2. search about the EC2

### 3. You need to config the UBUNTU Machine

### 4. Launch the instance

### 5. update the machine:
```
sudo apt update
```
```
sudo apt-get update
```
```
sudo apt upgrade -y
```
```
sudo apt install git curl unzip tar make sudo vim wget -y
```
```
git clone "Your-repository"
```
```
sudo apt install python3-pip
```
```
pip3 install -r requirements.txt
```
```
python3 -m streamlit run StreamlitAPP.py
```
### 6. if you want to add openai api key
```
create .env file in your server touch .env
```
### 7. vi .env #press insert #copy your api key and paste it there #press and then :wq and hit enter

### 8. Go with security and add the inbound rule add the port 8501

### Access the application in your web browser at the provided URL.

### Upload a PDF or text file containing the text you want to generate quizzes from.

### Enter the number of MCQs, subject, and complexity level, then click "Create MCQs".

### View the generated quiz and its evaluation.


# Acknowledgements
#### This project uses OpenAI's GPT-3.5 language model for text generation.
#### Streamlit is used for building the user interface.
#### AWS EC2 is used for App deployement
# Contact
#### For questions or inquiries, please contact maheshjadhav7979@gmail.com.
