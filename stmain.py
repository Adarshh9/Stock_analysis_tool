import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime , timedelta
import streamlit as st

def get_stock_data(ticker,start_date,end_date):
    stock_data = yf.download(tickers=ticker , start=start_date , end=end_date)
    return stock_data

def plot_stock_performance(stock_data , ticker):
    plt.figure(figsize=(6,4))
    plt.plot(stock_data["Close"] ,label=f"{ticker} Close Price" ,c="b")
    plt.title(f"{ticker} Stock Performance")
    plt.xlabel("Month")
    plt.ylabel("Stock Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.show()
    st.pyplot(plt)
        
def main():  
    st.title("Stock Performance")         
    current_date = datetime.today().date()                                                                                   
    start_date = current_date - timedelta(days=365)                                          
    end_date = current_date                                                 
    
    with st.container():
        col1 ,col2 , col3 , col4 , col5 = st.columns(5)
        if col1.button("NETFLIX"):
            stock_data = get_stock_data("NFLX",start_date,end_date)
            plot_stock_performance(stock_data,"NFLX")
        
        if col2.button("GOOGLE"):
            stock_data = get_stock_data("GOOGL",start_date,end_date)
            plot_stock_performance(stock_data,"GOOGL")
        
        if col3.button("TESLA"):
            stock_data = get_stock_data("TSLA",start_date,end_date)
            plot_stock_performance(stock_data,"TSLA")
        
        if col4.button("VISA"):
            stock_data = get_stock_data("V",start_date,end_date)
            plot_stock_performance(stock_data,"V")
            
        if col5.button("APPLE"):
            stock_data = get_stock_data("AAPL",start_date,end_date)
            plot_stock_performance(stock_data,"AAPL")
    
if __name__=="__main__":
    main()