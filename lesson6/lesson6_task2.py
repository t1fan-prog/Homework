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


def math(ing):
    global total_sum
    sum1 = stock[f"{ing}"] * prices[f"{ing}"]
    print(f"{ing}: {float(sum1)}")
    total_sum += sum1


print("Cost of each ingredient:\n")

for i in iter(stock.keys()):
    math(i)

print(f"\nTotal cost of the stock is {total_sum}")
