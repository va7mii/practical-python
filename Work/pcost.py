# pcost.py
#
# Exercise 1.27
prices = {
        'GOOG' : 490.1,
        'AA' : 23.45,
        'IBM' : 91.1,
        'MSFT' : 34.23
    }

print(prices.items())

# Inverting value-key pair
print(list(zip(prices.values(), prices.keys())))