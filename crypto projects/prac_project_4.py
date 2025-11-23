import requests

class CryptoPortfolio:

    def __init__(self, initial_holdings):
        self.holdings = initial_holdings
        self.current_prices = {}

    def fetch_live_prices(self):
        # live prices from the website
        try:
            coins = ",".join(self.holdings.keys())  # .keys is optional because python automatically provide the keys
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={coins}&vs_currencies=usd"
            response = requests.get(url)
            data = response.json()

            for coin in self.holdings:
                self.current_prices[coin] = data[coin]["usd"]
            print("Prices updated successfully!")

        except Exception as e:
            print(f"API Error!!!{e}")

    def calculate_total_value(self):
        # calculating total value
        total = 0
        for coin, data in self.holdings.items():
            current_price = self.current_prices.get(coin, 0)
            total += data["amount"] * current_price
        return total
    
    def calculate_profit_loss(self):
        # calculating profit loss
        pnl_report = {}
        for coin, data in self.holdings.items():
            current_price = self.current_prices.get(coin, 0)
            buy_value = data["amount"] * data["buy_price"]
            current_value = data["amount"] * current_price
            profit_loss = current_value - buy_value
            pnl_percentage = (profit_loss / buy_value) * 100

            pnl_report[coin] = {
                "profit_loss": profit_loss,
                "percentage": pnl_percentage,
                "current_value": current_value
            }
        return pnl_report
    
    def portfolio_summary(self):
        # summary of portfolio
        self.fetch_live_prices()
        total_value = self.calculate_total_value()
        pnl = self.calculate_profit_loss()

        print("\n" + "="*50)
        print("PORTFOLIO SUMMARY")
        print("="*50)

        for coin, data in self.holdings.items():
            current_price = self.current_prices[coin]
            coin_pnl = pnl[coin]

            print(f"\n{coin.upper()}:")
            print(f" Amount: {data["amount"]}")
            print(f" Buy price: ${data["buy_price"]:,.2f}")
            print(f" Current price: ${current_price:,.2f}")
            print(f" P/L: ${coin_pnl["profit_loss"]:,.2f} ({coin_pnl["percentage"]:+.2f}%)")

        print(f"\n Total portfolio value: ${total_value:,.2f}")

my_crypto = CryptoPortfolio({
    "bitcoin": {"amount": 0.1, "buy_price": 45000},
    "ethereum": {"amount": 2.5, "buy_price": 3500},
    "solana": {"amount": 16, "buy_price": 120}
})

my_crypto.portfolio_summary()