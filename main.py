import os
import streamlit as st
import pandas as pd
import json
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from langchain.llms import HuggingFaceHub
from langchain import PromptTemplate, LLMChain

# Set environment variable for protobuf
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

# Load datasets
stock_data = pd.read_csv('100_stock_data.csv', index_col='Date')
financial_data = pd.read_csv('financial_statements_fmp.csv')
news_data = pd.read_csv('news_articles_100_tickers.csv')

# Transform stock data to have a ticker column
stock_data = stock_data.reset_index().melt(id_vars='Date', var_name='ticker', value_name='price')

# Define prompt template
template = """
Based on the following data, provide an investment suggestion for the ticker {ticker}:
Stock Summary: {stock_summary}
Financial Summary: {financial_summary}
News Summary: {news_summary}

Suggestion:
"""

prompt = PromptTemplate(
    input_variables=["ticker", "stock_summary", "financial_summary", "news_summary"],
    template=template
)

# Load LLM from Hugging Face
llm = HuggingFaceHub(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    model_kwargs={"use_auth_token": "YOUR_HF_AUTH_TOKEN"},
    huggingfacehub_api_token="Replace with your HF key"
)

# Define LLM Chain
llm_chain = LLMChain(prompt=prompt, llm=llm)


def combine_data_for_ticker(ticker):
    stock_info = stock_data[stock_data['ticker'] == ticker].to_dict(orient='records')
    financial_info = financial_data[financial_data['ticker'] == ticker].to_dict(orient='records')
    news_info = news_data[news_data['ticker'] == ticker].to_dict(orient='records')

    stock_summary = f"Price data points: {len(stock_info)}"
    financial_summary = f"Latest report: {financial_info[0] if financial_info else 'No data'}"
    news_summary = f"News articles count: {len(news_info)}"

    combined_data = {
        'ticker': ticker,
        'stock_summary': stock_summary,
        'financial_summary': financial_summary,
        'news_summary': news_summary
    }

    return combined_data


def get_investment_suggestion(ticker):
    combined_data = combine_data_for_ticker(ticker)
    stock_summary = combined_data['stock_summary']
    financial_summary = combined_data['financial_summary']
    news_summary = combined_data['news_summary']

    suggestion = llm_chain.run(
        ticker=ticker,
        stock_summary=stock_summary,
        financial_summary=financial_summary,
        news_summary=news_summary
    )
    return suggestion


# Streamlit app
st.title("Investment Suggestion Chatbot")
st.write("Enter a ticker symbol to get an investment suggestion based on stock, financial, and news data.")

ticker_input = st.text_input("Ticker Symbol (e.g., AAPL)").upper()

if st.button("Get Suggestion"):
    if ticker_input:
        suggestion = get_investment_suggestion(ticker_input)
        st.write(f"Investment Suggestion for {ticker_input}:")
        st.write(suggestion)
    else:
        st.write("Please enter a ticker symbol.")
