# Commodity and Forex Hedging Tool

## Overview

This tool is designed to help users calculate the hedge ratio between a commodity and a forex pair based on historical returns. The hedge ratio provides an optimal exposure to the forex market for hedging against movements in commodity prices. It calculates the correlation and covariance between commodity returns and forex returns, and visualizes their relationship through a scatter plot. The tool is useful for traders, investors, and financial analysts who wish to hedge commodity exposure with forex instruments.

## Features

- **Hedge Ratio Calculation**: Determines the optimal amount of forex exposure needed to hedge against a commodity position.
- **Correlation Analysis**: Calculates the correlation between commodity returns and forex returns to assess their relationship.
- **Historical Data Retrieval**: Fetches historical price data for commodities and forex from Yahoo Finance.
- **Scatter Plot Visualization**: Visualizes the relationship between commodity and forex returns, with different colors for the two variables and a trend line.
- **User Input**: Allows users to input custom commodity exposure, tickers, and date ranges.

## Requirements

Before running this script, you need to install the following Python libraries:

- `numpy`: For numerical calculations.
- `pandas`: For data manipulation and handling.
- `yfinance`: To fetch historical financial data from Yahoo Finance.
- `matplotlib`: For plotting the scatter plot.

Install these libraries via `pip` if you don't already have them installed:

```bash
pip install numpy pandas yfinance matplotlib
```

## Installation

1. Ensure that Python is installed on your system (version 3.6 or higher).
2. Install the required packages by running:
   ```bash
   pip install numpy pandas yfinance matplotlib
   ```
3. Download or clone the Python script.

## How to Use the Tool

### Step 1: Input Parameters

Run the script, and the tool will prompt you for the following inputs:

- **Commodity Exposure (in USD)**: The amount of capital you have exposed to the commodity.
- **Commodity Ticker**: The ticker symbol of the commodity (e.g., `CL=F` for crude oil).
- **Forex Ticker**: The ticker symbol of the forex pair you wish to use for hedging (e.g., `EURUSD=X` for EUR/USD).
- **Start Date**: The start date for fetching historical data in the format `YYYY-MM-DD`.
- **End Date**: The end date for fetching historical data in the format `YYYY-MM-DD`.

Example input prompt:

```bash
Enter your commodity exposure (in USD): 1000000
Enter the commodity ticker (e.g., 'CL=F' for crude oil): CL=F
Enter the forex ticker (e.g., 'EURUSD=X'): EURUSD=X
Enter the start date for historical data (YYYY-MM-DD): 2021-01-01
Enter the end date for historical data (YYYY-MM-DD): 2024-01-01
```

### Step 2: Fetch Data

The tool will retrieve historical price data for the commodity and forex ticker from Yahoo Finance using the provided date range. It calculates the **daily returns** for both assets based on the adjusted closing price.

### Step 3: Hedge Ratio Calculation

The tool calculates the **hedge ratio** using the formula:

\[
\text{Hedge Ratio} = \frac{\text{Covariance(Commodity, Forex)}}{\text{Variance(Forex)}}
\]

This ratio tells you how much forex exposure is needed to hedge your commodity exposure.

### Step 4: Correlation Calculation

The tool calculates the **correlation coefficient** between the commodity and forex returns using the Pearson correlation formula:

\[
\text{Correlation} = \frac{\text{Covariance(Commodity, Forex)}}{\sigma_{\text{Commodity}} \cdot \sigma_{\text{Forex}}}
\]

The correlation value ranges between -1 (perfect negative correlation) and 1 (perfect positive correlation).

### Step 5: Results Output

The tool will display the following results:

- **Hedge Ratio**: The optimal amount of forex exposure required to hedge your commodity position.
- **Recommended Forex Exposure**: The amount of forex exposure in USD needed to hedge the commodity exposure.
- **Correlation**: The correlation between the returns of the commodity and the forex pair.

Example output:

```bash
Results:
Hedge Ratio: -0.2350
Recommended Forex Exposure for Hedging: -235000 USD
Correlation Between Commodity and Forex Returns: -0.0490
```

### Step 6: Visualization

The tool generates a **scatter plot** to visualize the relationship between the commodity and forex returns. The data points for commodity returns are shown in **blue**, while the forex returns are shown in **orange**. A **line** is traced through the commodity data points to show the trend.

- **Blue Data Points**: Represent commodity returns.
- **Orange Data Points**: Represent forex returns.
- **Line**: Traced through the commodity returns to show the trend.

### Example Scatter Plot

The scatter plot displays the following:
- **x-axis**: Forex returns.
- **y-axis**: Commodity returns.
- The plot is accompanied by a title, labels for both axes, and a grid.

## Example of a Complete Session

```bash
Commodity and Forex Hedging Tool
----------------------------------------
Enter your commodity exposure (in USD): 1000000
Enter the commodity ticker (e.g., 'CL=F' for crude oil): CL=F
Enter the forex ticker (e.g., 'EURUSD=X'): EURUSD=X
Enter the start date for historical data (YYYY-MM-DD): 2021-01-01
Enter the end date for historical data (YYYY-MM-DD): 2024-01-01

Fetching data...
Results:
Hedge Ratio: -0.2350
Recommended Forex Exposure for Hedging: -235000 USD
Correlation Between Commodity and Forex Returns: -0.0490

Note: This calculation assumes a linear relationship between commodity and forex returns.
Hedging recommendations are based on historical data and may not reflect future market conditions.
```

### Plot:
After the results, a scatter plot will be displayed showing the relationship between commodity and forex returns.

## Code Details

- **fetch_data**: Fetches historical adjusted closing price data for the commodity and forex tickers using `yfinance.download()`. It calculates the percentage returns and returns the cleaned data.
- **calculate_hedge_ratio**: Computes the hedge ratio based on covariance and variance.
- **calculate_correlation**: Computes the Pearson correlation coefficient between commodity and forex returns.
- **align_data**: Aligns the returns data for both the commodity and forex using the common date range.
- **plot_relationship**: Generates a scatter plot using `matplotlib` and plots a line through the commodity returns.

## Limitations

- **Data Accuracy**: The accuracy of the results depends on the quality and availability of the data fetched from Yahoo Finance.
- **Past Performance**: The hedge ratio and correlation are based on historical data and may not be indicative of future performance.
- **Linear Assumption**: The calculations assume a linear relationship between commodity and forex returns, which may not always hold in real markets.

## Future Enhancements

- **Additional Visualizations**: Include additional plots such as time series plots, rolling correlations, or volatility analysis.
- **Risk Management**: Incorporate risk management techniques such as Value at Risk (VaR) or Monte Carlo simulations.
- **User Customization**: Allow users to input multiple commodities and forex pairs for diversified hedging strategies.

## Conclusion

This tool provides a straightforward way to calculate the hedge ratio between commodities and forex pairs, helping users manage their risk exposure in both markets. It uses historical data and simple statistical techniques to derive meaningful hedging recommendations and visual insights.

