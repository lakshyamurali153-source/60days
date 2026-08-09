max_profit = 0
buy_price = 0
sell_price = 0
min_price = float('inf')
prices = list(map(float, input("Enter the stock prices separated by spaces: ").split()))
for price in prices:
    if price < min_price:
        min_price = price
      
    elif price - min_price > max_profit:
        max_profit = price - min_price
        buy_price = min_price  
        sell_price = price

if max_profit > 0:
    print(f"Buy at: {buy_price}, Sell at: {sell_price}, Max Profit: {max_profit}")
else:
    print("No profitable transaction possible.")
