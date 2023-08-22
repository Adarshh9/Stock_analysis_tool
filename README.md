# Stock Data Visualization and Web App

This repository contains two sets of Python scripts for fetching stock data, visualizing it using Matplotlib, and creating a Streamlit web app for interactive visualization.

## Table of Contents

- [Description](#description)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Streamlit Web App](#streamlit-web-app)
- [Contributing](#contributing)

## Description

The project includes two main sets of functionality:

1. **Stock Data Fetching and Matplotlib Visualization:** The script `fetch_stock_data.py` fetches stock data using the Yahoo Finance API (`yfinance` library) and visualizes it using Matplotlib. The fetched data is saved to a CSV file named after the stock ticker. The stock performance graph displays the closing price over time.

2. **Interactive Stock Performance Web App with Streamlit:** The script `streamlit_stock_app.py` creates a Streamlit web app for interactive stock performance visualization. The app fetches stock data for various stock tickers, and users can select different companies to view their stock performance graphs.

## Getting Started

1. Clone the repository to your local machine:

   ```bash
   git clone [https://github.com/YourUsername/StockVisualization.git](https://github.com/Adarshh9/Stock_analysis_tool.git)
   ```

2. Install the required Python libraries:

   ```bash
   pip install yfinance pandas matplotlib streamlit
   ```

## Usage

### Stock Data Fetching and Matplotlib Visualization

1. Run the stock data fetching and visualization script:

   ```bash
   python main.py
   ```

   Follow the prompts to provide the stock ticker and date range.

2. The script will save the stock data as a CSV file and display the stock performance graph using Matplotlib.

### Streamlit Web App

1. Start the Streamlit web app:

   ```bash
   streamlit run stmain.py
   ```

2. The web app will open in your default web browser.

3. Click on the buttons for different companies to view their stock performance graphs interactively.

## Contributing

Contributions to this project are encouraged. If you encounter issues or want to enhance the project, feel free to create a pull request.

---
