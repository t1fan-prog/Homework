# Create a function which takes as input two dicts with structure mentioned above,
# then computes and returns the total price of stock.


stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_sum = 0

print("Cost of each ingredient:\n")

for key in stock:
    sum1 = stock[f"{key}"] * prices[f"{key}"]
    print(f"{key}: {float(sum1)}")
    total_sum += sum1

print(f"\nTotal cost of the stock is {total_sum}")