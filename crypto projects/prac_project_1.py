#crypto portfolio

#porfolio data
portfolio = {
    "btc": {"amount":0.5, "buy_price":45000},
    "eth": {"amount":3.2, "buy_price":3500},
    "sol": {"amount":15.7, "buy_price":180},
    "link": {"amount":10 , "buy_price":11}
}

#current price
current_prices = {
    "btc": 52000,
    "eth": 3800,
    "sol": 210,
    "link": 17
}

def calculate_portfolio_value():
    total_value = 0
    print("=== YOUR CRYPTO PORTFOLIO ===")

    for coin, data in portfolio.items():
        current_price = current_prices[coin]
        current_value = data["amount"] * current_price
        profit_loss = current_value - (data["amount"] * data["buy_price"])

        print(f"{coin}:")
        print(f"  Amount: {data["amount"]}")
        print(f"  Current values: ${current_value:,.2f}")
        print(f"  P/L: ${profit_loss:,.2f}")
        print()

        total_value = total_value + current_value

    print(f"TOTAL PORTFOLIO VALUE: ${total_value:,.2f}")

calculate_portfolio_value()