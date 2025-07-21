# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

portfolio = {}

print("Enter your stock holdings (type 'done' to finish):")
while True:
    stock = input("Stock symbol: ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found. Available stocks:", ", ".join(stock_prices.keys()))
        continue
    try:
        qty = int(input(f"Quantity of {stock}: "))
        if qty < 0:
            print("Quantity must be non-negative.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + qty
    except ValueError:
        print("Please enter a valid integer for quantity.")

# Calculate total investment
total_investment = sum(stock_prices[symbol] * qty for symbol, qty in portfolio.items())

print("\nYour Portfolio:")
for symbol, qty in portfolio.items():
    print(f"{symbol}: {qty} shares @ ${stock_prices[symbol]} each = ${stock_prices[symbol] * qty}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optionally save to file
save = input("Save results to file? (y/n): ").lower()
if save == 'y':
    filename = input("Enter filename (e.g., portfolio.txt or portfolio.csv): ")
    if filename.endswith('.csv'):
        with open(filename, 'w') as f:
            f.write("Stock,Quantity,Price,Value\n")
            for symbol, qty in portfolio.items():
                value = stock_prices[symbol] * qty
                f.write(f"{symbol},{qty},{stock_prices[symbol]},{value}\n")
            f.write(f"Total,,,{total_investment}\n")
    else:
        with open(filename, 'w') as f:
            f.write("Your Portfolio:\n")
            for symbol, qty in portfolio.items():
                value = stock_prices[symbol] * qty
                f.write(f"{symbol}: {qty} shares @ ${stock_prices[symbol]} each = ${value}\n")
            f.write(f"\nTotal Investment Value: ${total_investment}\n")
    print(f"Results saved to {filename}")