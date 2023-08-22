import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime , timedelta

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
        
if __name__=="__main__":           
    current_date = datetime.today().date()                                    
    stock_ticker = "AAPL"                                                  
    start_date = current_date - timedelta(days=365)                                          
    end_date = current_date                                                 
                                                                        
    stock_data = get_stock_data(stock_ticker,start_date,end_date)             
                                                                            
    df = pd.DataFrame.copy(stock_data)                                        
    df.to_csv(f"{stock_ticker}.csv",index=False)                              
                                                                        
    print(stock_data)
    
    plot_stock_performance(stock_data,stock_ticker)