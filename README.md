
# Crypto Trading Dashboard with Backtesting and Visualization

This Streamlit-based application provides an interactive dashboard for analyzing cryptocurrency price data, implementing trading strategies, and visualizing results. It includes features for uploading custom datasets, applying filters, and evaluating performance metrics using backtesting. The application is designed to help traders and analysts make data-driven decisions.

---

## Features

- **Upload Custom Data**: Upload your CSV file with columns: `Date`, `Open`, `High`, `Low`, and `Close`.
- **Price Filtering**: Filter data by specifying a minimum and maximum price range.
- **Moving Average Strategy**: Generate buy/sell signals based on moving average crossover strategies.
- **Backtesting**: Simulate trading strategies and calculate:
  - Total Return
  - Maximum Drawdown
  - Sharpe Ratio
- **Interactive Charts**:
  - Line chart with buy/sell signals
  - Portfolio equity curve
  - Candlestick chart
- **Default Data**: Use pre-loaded data (`data.pkl`) as a fallback for convenience.

---

## How to Run

### - Prerequisites
1. **Python 3.9+** installed on your machine.
2. Install the required Python packages using `requirements.txt`.

### - Setup Instructions
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the application:
   ```bash
   streamlit run app.py

4. Open the application in your browser at http://localhost:8501.


---


###  # Data Requirements

###  - Default Data

  - The default dataset is loaded from data.pkl. Ensure it contains the following columns:
      - Date (formatted as YYYY-MM-DD and set as the index)
      - Open, High, Low, and Close prices.

### - Custom Data

  - Upload a CSV file via the sidebar with the required columns: Date, Open, High, Low, and Close.
  - Note: Prices should be in USD.
  

### - Usage Guide

###  - Sidebar Parameters

  * Upload Data: Upload your dataset or use the default dataset.
  * Filters:
        - Set minimum and maximum price ranges.
        - Adjust the moving average window size (5–50 days).
        - Define the starting capital for backtesting.
   * Performance Metrics: View total return, maximum drawdown, and Sharpe ratio.

### - Visualization

  - Price Chart: Shows the price movement with buy/sell signals.
  - Portfolio Equity Curve: Displays the portfolio value over time.
  - Candlestick Chart: Offers detailed price action analysis.

---

### - File Structure
    ```bash
      ├── app.py                 # Main application file
      ├── data.pkl               # Default dataset (pickle format)
      ├── ethe.csv               # Example CSV dataset
      ├── requirements.txt       # Python dependencies
      └── README.md              # Project documentation

---

### - Requirements

  - Install dependencies using the provided requirements.txt:
    ```bash
     altair==5.4.1
     numpy==2.1.3
     pandas==2.2.3
     plotly==5.24.1
     streamlit==1.40.1
     ...

---

  ### - Interactive Price Chart : 
  
  ![buy-sell price chart ethe](https://github.com/user-attachments/assets/e4f1c399-2179-415d-bb40-8c2e17886e5e)


---


  ### - Portfolio Equity Curve : 
  
  ![portfolo equity curve ethe](https://github.com/user-attachments/assets/a79d7325-d952-4158-ad90-b5f4c677b2d9)


---


  ### - Candlestick Chart : 
  
  ![candelstick_chart ethe](https://github.com/user-attachments/assets/581bf4e1-5cf9-438c-820a-c63f7fa1a9dc)


  
---


### * License

This project is open-source and available under the **MIT License**.





