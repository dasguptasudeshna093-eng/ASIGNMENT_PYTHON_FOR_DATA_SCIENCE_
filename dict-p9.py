
stock = {"pen": 10, "book": 5, "bag": 2}

transactions = [
    {"type": "receive", "item": "pen", "quantity": 4},
    {"type": "sell", "item": "book", "quantity": 3},
    {"type": "sell", "item": "bag", "quantity": 5},
    {"type": "receive", "item": "ruler", "quantity": 6},
    {"type": "sell", "item": "pen", "quantity": 8}
]

accepted = 0
rejected = 0

for transaction in transactions:

    action = transaction["type"]
    item = transaction["item"]
    quantity = transaction["quantity"]

    if action == "receive":

        if item in stock:
            stock[item] += quantity
        else:
            stock[item] = quantity

        accepted += 1

    elif action == "sell":

        if item in stock and stock[item] >= quantity:
            stock[item] -= quantity
            accepted += 1
        else:
            print("Sale rejected:", item)
            rejected += 1

print("Final stock:", stock)
print("Accepted transactions:", accepted)
print("Rejected transactions:", rejected)
