import requests

class CryptoPortfolio:
    def __init__(self):
        self.holdings = {}
        self.current_prices = {}

    def fetch_live_prices(self):
        try:
            coinnames = ",".join(self.holdings)
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={coinnames}&vs_currencies=usd"
            response = requests.get(url)
            data = response.json()

            for coin in self.holdings:
                self.current_prices[coin] = data[coin]["usd"]
            print("Prices updated successfully!")

        except Exception as e:
            print(f"API error!!!:{e}")

    def calculate_total_value(self):
        total = 0 
        for coin, data in self.holdings.items():
            current_price = self.current_prices.get(coin, 0)
            total = total + data["amount"] * current_price
        return total
    
    def calculate_profit_loss(self):
        pnl_report = {}
        for coin, data in self.holdings.items():
            current_price = self.current_prices.get(coin, 0)
            buy_value = data["amount"] * data["buy_price"]
            current_value = data["amount"] * current_price
            profit_loss = current_value - buy_value
            pnl_percentage = (profit_loss / buy_value) * 100

            pnl_report[coin] = {
                "profit_loss" : profit_loss,
                "percentage" : pnl_percentage,
                "current_value" : current_value
            }
        return pnl_report
    
    def portfolio_summary(self):
        self.fetch_live_prices()
        total_value = self.calculate_total_value()
        pnl = self.calculate_profit_loss()

        print("\n" + "=" * 50)
        print("PORTFOLIO SUMMARY")
        print("=" * 50)

        for coin, data in self.holdings.items():
            current_price = self.current_prices[coin]
            coin_pnl = pnl[coin]

            print(f"\n{coin.upper()}:")
            print(f" Amount: {data["amount"]}")
            print(f" Buy Price: ${data["buy_price"]:,.2f}")
            print(f" Current Price: ${current_price:,.2f}")
            print(f" P/L: ${coin_pnl["profit_loss"]:,.2f} ({coin_pnl["percentage"]:,.2f}%)")

        print(f"\nTOTAL PORTFOLIO VALUE: ${total_value:,.2f}")

    def interactive_add_coin(self, coin_name=None, amount=None, buy_price=None):
        if coin_name is None:
            coin_name = input("Coin Name: ").strip().lower()
            amount = float(input("Amount you hold: "))
            buy_price = float(input("Your buy price: $"))

        self.holdings[coin_name] = {
            "amount" : amount,
            "buy_price" : buy_price
        }

        print(f"Successfully added {amount} {coin_name} at ${buy_price:,.2f}")

def add_coin_flow(portfolio):
    print("\n" + "=" * 30)
    print("ADD NEW COIN")
    print("=" * 30)

    while True:
        coin_name = input("Coin name or ('done' to finish): ").strip().lower()

        if coin_name == "done":
            break

        try:
            amount = float(input("Amount: "))
            buy_price = float(input("Buy price: $"))

            portfolio.interactive_add_coin(coin_name, amount, buy_price)

            another = input("Add another coin? (y/n): ").strip().lower()
            if another != "y":
                break

        except ValueError:
            print("Invalid input! Please enter numbers for amount and price.")

def remove_coin_flow(portfolio):
    if not portfolio.holdings:
        print("Portfolio is empty!")
        return
    
    print("\nYour coins:", list(portfolio.holdings.keys())) 

    coin_name = input("Enter coin to remove: ").strip().lower()

    if coin_name in portfolio.holdings:
        del portfolio.holdings[coin_name]
        print(f"Removed {coin_name} from portfolio!")
    else:
        print(f"{coin_name} not found in portfolio")

def run_portfolio_manager():
    portfolio = CryptoPortfolio()

    while True:
        print("\n" + "=" * 50)
        print("CRYPTO PORTFOLIO MANAGER")
        print("=" * 50)
        print("1. Add coin")
        print("2. Remove coin")
        print("3. View portfolio summary")
        print("4. Exit")

        choice = input("\nChoose option (1-4): ").strip()

        if choice == "1":
            add_coin_flow(portfolio)
        elif choice == "2":
            remove_coin_flow(portfolio)
        elif choice == "3":
            portfolio.portfolio_summary()
        elif choice == "4":
            print("Thanks for using Crypto Portfolio Manager!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    run_portfolio_manager()

