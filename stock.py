# 1. Hardcoded dictionary defining stock prices
stock_prices = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "NVDA": 130.0,
    "MSFT": 420.0
}

print("--- Welcome to the Stock Portfolio Tracker ---")
print(f"Available stocks to track: {list(stock_prices.keys())}\n")

# 2. Get user input
ticker = input("Enter the stock ticker (e.g., AAPL): ").upper().strip()

# Check if the stock exists in our dictionary
if ticker in stock_prices:
    try:
        quantity = int(input(f"Enter the quantity of {ticker} shares you own: "))
        
        # 3. Perform basic arithmetic calculation
        price_per_share = stock_prices[ticker]
        total_value = quantity * price_per_share
        
        # Display the result
        print("\n--- Portfolio Summary ---")
        print(f"Stock: {ticker}")
        print(f"Quantity: {quantity}")
        print(f"Current Price: ${price_per_share}")
        print(f"Total Investment Value: ${total_value:,.2f}")
        
        # 4. Optional: Save the result to a text file
        save_choice = input("\nDo you want to save this to a file? (yes/no): ").lower().strip()
        if save_choice == 'yes':
            with open("portfolio_summary.txt", "w") as file:
                file.write(f"Stock Portfolio Summary\n")
                file.write(f"-----------------------\n")
                file.write(f"Stock: {ticker}\n")
                file.write(f"Quantity: {quantity}\n")
                file.write(f"Total Value: ${total_value:,.2f}\n")
            print("Successfully saved to 'portfolio_summary.txt'!")
            
    except ValueError:
        print("Error: Please enter a valid whole number for the quantity.")
else:
    print(f"Error: Stock '{ticker}' is not found in the system.")
