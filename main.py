import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def calculate_hedge_ratio(commodity_returns, forex_returns):
    """Calculate hedge ratio based on historical returns."""
    covariance = np.cov(commodity_returns, forex_returns)[0][1]
    variance = np.var(forex_returns)
    hedge_ratio = covariance / variance
    return hedge_ratio

def calculate_correlation(commodity_returns, forex_returns):
    """Calculate correlation between commodity and forex returns."""
    correlation = np.corrcoef(commodity_returns, forex_returns)[0, 1]
    return correlation

def fetch_data(ticker, start_date, end_date):
    """Fetch historical data for a given ticker."""
    data = yf.download(ticker, start=start_date, end=end_date)
    close_column = 'Adj Close' if 'Adj Close' in data.columns else 'Close'
    if close_column not in data.columns:
        raise ValueError(f"Data for {ticker} does not contain 'Adj Close' or 'Close'. Please check the ticker symbol.")
    data['Returns'] = data[close_column].pct_change()
    return data['Returns'].dropna()

def align_data(commodity_returns, forex_returns):
    """Align two return series by their indices."""
    aligned_data = pd.concat([commodity_returns, forex_returns], axis=1, join='inner', keys=['Commodity', 'Forex'])
    return aligned_data['Commodity'], aligned_data['Forex']

def plot_relationship(commodity_returns, forex_returns):
    """Plot the relationship between commodity and forex returns."""
    plt.figure(figsize=(8, 6))

    # Plotting commodity returns in blue
    plt.scatter(forex_returns, commodity_returns, alpha=0.7, color='blue', label="Commodity Returns")
    
    # Plotting a line for commodity returns
    plt.plot(forex_returns, commodity_returns, color='blue', alpha=0.5)  # Tracing the line for the commodity

    # Plotting forex returns in orange
    plt.scatter(forex_returns, forex_returns, alpha=0.7, color='orange', label="Forex Returns")
    
    plt.title("Relationship Between Commodity and Forex Returns")
    plt.xlabel("Forex Returns")
    plt.ylabel("Commodity Returns")
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    plt.axvline(0, color='gray', linestyle='--', linewidth=0.8)
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()

def main():
    print("\nCommodity and Forex Hedging Tool")
    print("-" * 40)

    # Inputs
    try:
        commodity_exposure = float(input("Enter your commodity exposure (in USD): "))
        commodity_ticker = input("Enter the commodity ticker (e.g., 'CL=F' for crude oil): ")
        forex_ticker = input("Enter the forex ticker (e.g., 'EURUSD=X'): ")
        start_date = input("Enter the start date for historical data (YYYY-MM-DD): ")
        end_date = input("Enter the end date for historical data (YYYY-MM-DD): ")
    except ValueError:
        print("Invalid input. Please enter valid numeric values and strings.")
        return

    # Fetch Data
    print("\nFetching data...")
    try:
        commodity_returns = fetch_data(commodity_ticker, start_date, end_date)
        forex_returns = fetch_data(forex_ticker, start_date, end_date)
        commodity_returns, forex_returns = align_data(commodity_returns, forex_returns)
    except Exception as e:
        print(f"Error fetching data: {e}")
        return

    # Hedge Ratio Calculation
    hedge_ratio = calculate_hedge_ratio(commodity_returns, forex_returns)
    forex_exposure = commodity_exposure * hedge_ratio

    # Correlation Calculation
    correlation = calculate_correlation(commodity_returns, forex_returns)

    # Results Output
    print("\nResults:")
    print(f"Hedge Ratio: {hedge_ratio:.4f}")
    print(f"Recommended Forex Exposure for Hedging: {forex_exposure:.2f} USD")
    print(f"Correlation Between Commodity and Forex Returns: {correlation:.4f}")

    # Plot Relationship between Commodity and Forex Returns
    plot_relationship(commodity_returns, forex_returns)

    print("\nNote: This calculation assumes a linear relationship between commodity and forex returns.")
    print("Hedging recommendations are based on historical data and may not reflect future market conditions.")

if __name__ == "__main__":
    main()
