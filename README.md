# Financial_Suggestion
Financial_Suggestion
This project aims to develop an investment suggestion chatbot that uses stock, financial, and news data to provide investment recommendations for specific ticker symbols. The chatbot is implemented using Streamlit for the web interface and integrates Hugging Face models via LangChain for generating suggestions.

Project Overview
The Investment Suggestion Chatbot leverages stock price data, financial statements, and news articles to provide investment advice. The system utilizes a pre-trained model from Hugging Face to generate recommendations based on the provided data. The user inputs a ticker symbol, and the chatbot retrieves relevant data to generate an informed suggestion.


tickers = [
    'AAPL', 'MSFT', 'NVDA', 'GOOGL', 'AI', 'GOOG', 'AMZN', 'META', 'TSM', 'TSLA', 
    'PINS', 'IBM', 'PFE', 'VZ', 'PDD', 'DIS', 'NOW', 'BABA', 'BX', 'MS', 
    'AMAT', 'CAT', 'GS', 'NEE', 'ISRG', 'HSBC', 'CMCSA', 'RTX', 'RY', 'TTE', 
    'UL', 'SPGI', 'UNP', 'HDB', 'T', 'BHP', 'LOW', 'HON', 'LMT', 'VRTX', 
    'SNY', 'MUFG', 'TJX', 'BLK', 'UBER', 'ARM', 'SYK', 'COP', 'PGR', 'BUD', 
    'BKNG', 'INTC', 'ELV', 'C', 'ETN', 'REGN', 'PLD', 'SCHW', 'MU', 'UPS', 
    'NKE', 'BSX', 'MMC', 'CB', 'BA', 'RIO', 'ADI', 'LRCX', 'ADP', 'AMT', 
    'KKR', 'ANET', 'MDT', 'SONY', 'PANW', 'TD', 'KLAC', 'IBN', 'MMM', 'GILD', 
    'PEP', 'ABT', 'MRK', 'WMT', 'KO', 'CMG', 'MCD', 'JNJ', 'V', 'MA', 
    'PYPL', 'NFLX', 'ADBE', 'CRM', 'CSCO', 'ORCL', 'SAP', 'INTU', 'AMD', 'QCOM'
]


Installation
To get started with the project, follow these steps:

Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/investment-suggestion-chatbot.git
cd investment-suggestion-chatbot
Create a Virtual Environment:

Create a Virtual Environment:

bash
Copy code
python -m venv llm_finance_env
source llm_finance_env/bin/activate   # On Windows: llm_finance_env\Scripts\activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
To run the Streamlit application:

Set Environment Variables:
Set the environment variable for the Protobuf implementation:

python
Copy code
import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
Run Streamlit App:

bash
Copy code
streamlit run app.py
Interact with the Chatbot:
Open the URL provided by Streamlit and enter a ticker symbol to get an investment suggestion.

Stock Data
Download historical stock price data for 100 ticker symbols using Yahoo Finance.
Save the data in a CSV file named 100_stock_data.csv.
Financial Data
Fetch financial statements for the tickers using the Alpha Vantage API.
Save the data in a CSV file named financial_statements_fmp.csv.
News Data
Scrape news articles related to the tickers using various news sources.
Save the articles in a CSV file named news_articles_100_tickers.csv.
Model and LLM Integration
Load and Prepare Data
Load the datasets into pandas DataFrames.
Transform the stock data to have a ticker column.
Combine data for each ticker to prepare inputs for the LLM.
Define Prompt Template
Define a prompt template that structures the data inputs for the LLM to generate investment suggestions.

Initialize Hugging Face Model
Load the pre-trained model from Hugging Face using LangChain’s HuggingFaceHub interface.

Define LLM Chain
Create an LLM Chain using the defined prompt template and the loaded model.

Generate Investment Suggestion
Use the combined data and LLM Chain to generate investment suggestions based on user input.

Streamlit Application
The Streamlit application provides a user-friendly interface for interacting with the chatbot. Users can input a ticker symbol, and the chatbot will display an investment suggestion based on the retrieved data.

Future Work
Enhance Data Sources: Integrate more comprehensive and real-time data sources.
Improve Model Accuracy: Fine-tune the LLM with domain-specific data to improve accuracy.
Expand Functionality: Add features like portfolio management and risk assessment.
