# llm_portfolio_recommendation
 A Streamlit app using Langchain and OpenAI API to generate a financial portfolio recommendation based on a country and bond types

We'll structure the project into three main files:

streamlit_app.py: The main Streamlit app file that interacts with the user and presents the output.

langchain_code.py: This Python script will implement Langchain logic using OpenAI to get bond recommendations.

config.py: This file stores the OpenAI API key for authentication.

# Instructions for Running the App

### 1. Setup API Key
Make sure you have your OpenAI API key ready. Place it in the `config.py` file as shown below:

OPENAI_API_KEY = 'your-openai-api-key-here'

### 2.  Install Dependencies
Install the necessary Python libraries by running:

pip install -r requirements.txt

### 3. Run Streamlit App
In the terminal, navigate to the folder containing the files and run:

streamlit run streamlit_app.py


