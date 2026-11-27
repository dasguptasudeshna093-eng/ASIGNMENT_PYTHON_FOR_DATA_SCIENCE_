
sales = [
    {"product": "Pen", "quantity": 3, "price": 15},
    {"product": "Book", "quantity": 2, "price": 120},
    {"product": "Pen", "quantity": 5, "price": 15},
    {"product": "Bag", "quantity": 1, "price": 850},
    {"product": "Book", "quantity": -1, "price": 120},
    {"product": "Ruler", "quantity": 4, "price": 20}]
revenue = {}
total = 0
invalid = 0
high = []

for i in sales:
    if i["quantity"] <= 0 or i["price"] < 0:
        invalid += 1
        continue

    r = i["quantity"] * i["price"]
    p = i["product"]

    revenue[p] = revenue.get(p, 0) + r
    total += r
    if r >= 200:
        high.append(p)

highest = max(revenue, key=revenue.get)

print(revenue)
print("Total:", total)
print("Highest:", highest)
print("High revenue:", high)
print("Invalid:", invalid)
