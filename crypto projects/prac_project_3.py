import requests

# portfoilio
my_coins = {
    "bitcoin" : 0.5,
    "ethereum" : 3.2,
    "solana" : 13
}

def get_coin_prices(coin_name):
    # get prices from the internet
    try:
        #ask web for price
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_name}&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        return data[coin_name]["usd"]
    except:
        return None
    
def show_my_portfolio():
    # show the worth of my portfolio
    print(" YOUR LIVE CRYPTO PORTFOLIO")
    print("fetching prices.....\n")

    total_value = 0

    for coin, amount in my_coins.items():
        price = get_coin_prices(coin)

        if price:
            value = amount * price
            total_value += value
            print(f"{coin.upper()}:")
            print(f" You own: {amount} coins")
            print(f" Current price: ${price:,.2f}")
            print(f" Value: ${value:,.2f}\n")
        else:
            print(f"{coin.upper()}: could not get the price\n")

    print(f" TOTAL VALUE: ${total_value:,.2f}")

show_my_portfolio()