portfolio = {
    "btc": {"amount": 0.5, "buy_price": 45000, "current_price": 52000},
    "eth": {"amount": 3.2, "buy_price": 3500, "current_price": 3800},
    "sol": {"amount": 15.7, "buy_price": 180, "current_price": 150},
    "link": {"amount": 20, "buy_price": 15, "current_price": 15}
}

def check_profit_loss():
    print("=== PORTFOLIO OVERVIEW ===")
    total_value = 0
    total_invested = 0

    for coin, data in portfolio.items():
        current_value = data["amount"] * data["current_price"]
        invested = data["amount"] * data["buy_price"]
        profit_loss = current_value - invested

        total_value += current_value
        total_invested += invested

        print(f"\n{coin.upper()}:")
        print(f" Invested: ${invested:,.2f}")
        print(f" Current: ${current_value:,.2f}")
        print(f" P/L: ${profit_loss:,.2f}")

    total_pnl = total_value - total_invested
    print(f"\n TOTAL PORTFOLIO:")
    print(f" Total Invested: ${total_invested:,.2f}")
    print(f" Total Current: ${total_value:,.2f}")
    print(f" Total P/L: ${total_pnl:,.2f}")

check_profit_loss()
