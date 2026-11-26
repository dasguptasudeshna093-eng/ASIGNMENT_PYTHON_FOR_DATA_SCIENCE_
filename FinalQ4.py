products = {"rice": 75, "milk": 90, "bread": 55, "egg": 15, "apple": 180, "oil": 190, "sugar": 130, "salt": 45, "soap": 60, "tea": 220}
for name, price in products.items():
    print(name, ":", price)
cart = {}
while True:
    name = input("Enter product (or done): ").lower()

    if name == "done":
        break
    if name not in products:
        print("Product not available")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Invalid quantity")
        continue
    cart[name] = cart.get(name, 0) + quantity

grand_total = 0

print("\nProduct  Price  Quantity  Total")

for name, quantity in cart.items():
    price = products[name]
    total = price * quantity

    print(name, price, quantity, total)

    grand_total += total
print("Grand Total:", grand_total)
