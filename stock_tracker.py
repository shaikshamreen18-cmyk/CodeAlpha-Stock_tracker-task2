# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 320
}

print("📈 Stock Portfolio Tracker")

stock = input("Enter Stock Name (AAPL/TSLA/GOOGL/MSFT): ").upper()

if stock in stock_prices:
    quantity = int(input("Enter Quantity: "))

    total = stock_prices[stock] * quantity

    print("\n----- Portfolio Summary -----")
    print("Stock Name :", stock)
    print("Price      :", stock_prices[stock])
    print("Quantity   :", quantity)
    print("Total Value:", total)

    # Save result to file
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write(f"Stock Name : {stock}\n")
        file.write(f"Price      : {stock_prices[stock]}\n")
        file.write(f"Quantity   : {quantity}\n")
        file.write(f"Total Value: {total}\n")

    print("\n✅ Portfolio saved to portfolio.txt")

else:
    print("❌ Invalid Stock Name!")