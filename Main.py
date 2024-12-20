import yfinance as yf
import pandas as pd
import datetime

def fetch_historical_data(tickers):
    data = {}
    for ticker in tickers:
        try:
            stock_data = yf.download(ticker, period="max")
            data[ticker] = stock_data
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
    return data

def analyze_stock(stock_data, ath_drawdown, consolidation_years):
    results = []
    for ticker, data in stock_data.items():
        data['AllTimeHigh'] = data['Close'].cummax()
        data['Drawdown'] = (data['Close'] - data['AllTimeHigh']) / data['AllTimeHigh'] * 100

        for i in range(len(data) - 252):  # Iterate till the last one-year back
            current_date = data.index[i]
            one_year_later_date = current_date + datetime.timedelta(days=365)

            if one_year_later_date not in data.index:
                continue

            # Condition 1: Drawdown
            if data['Drawdown'].iloc[i] <= -ath_drawdown:
                returns = (data['Close'].loc[one_year_later_date] / data['Close'].iloc[i]) - 1
                results.append({
                    'Ticker': ticker,
                    'Condition': f"{ath_drawdown}% Drawdown",
                    'Date': current_date,
                    'Return_1Y': returns
                })

            # Condition 2: Consolidation
            consolidation_start = current_date - datetime.timedelta(days=consolidation_years * 365)
            if consolidation_start in data.index and data.index[i] in data.index:
                consolidation_period_data = data.loc[consolidation_start:data.index[i], 'Close']
                if abs(consolidation_period_data.pct_change().sum()) < 0.05:  # Assuming 5% as "no change"
                    returns = (data['Close'].loc[one_year_later_date] / data['Close'].iloc[i]) - 1
                    results.append({
                        'Ticker': ticker,
                        'Condition': f"Consolidated for {consolidation_years} years",
                        'Date': current_date,
                        'Return_1Y': returns
                    })

    return pd.DataFrame(results)

def calculate_success_rate(results, success_threshold):
    if results.empty:
        return 0, 0
    successful_cases = results[results['Return_1Y'] >= success_threshold]
    success_rate = len(successful_cases) / len(results) * 100
    return len(successful_cases), success_rate

def main():
    tickers = input("Enter tickers separated by commas: ").split(',')
    tickers = [ticker.strip() for ticker in tickers]

    ath_drawdown = float(input("Enter the drawdown percentage (e.g., 20 for 20%): "))
    consolidation_years = int(input("Enter the consolidation period in years: "))
    success_threshold = float(input("Enter the percentage return considered as good (e.g., 0.1 for 10%): "))

    stock_data = fetch_historical_data(tickers)
    results = analyze_stock(stock_data, ath_drawdown, consolidation_years)

    if not results.empty:
        print(results)
        successful_cases, success_rate = calculate_success_rate(results, success_threshold)
        print(f"Total Successful Cases: {successful_cases}")
        print(f"Success Rate: {success_rate:.2f}%")
        results.to_csv("backtest_results.csv", index=False)
        print("Results saved to backtest_results.csv")
    else:
        print("No results found for the given conditions.")

if __name__ == "__main__":
    main()
