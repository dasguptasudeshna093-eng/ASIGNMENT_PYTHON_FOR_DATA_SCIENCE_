prices = {"rice": 75, "oil": 185, "sugar": 120, "milk": 95, "egg": 12, "flour": 65, "salt": 40, "lentil": 130, "potato": 45, "onion": 80,
    "tea": 250, "coffee": 450, "biscuit": 50, "soap": 70, "shampoo": 180}

print("=== AVAILABLE PRODUCTS ===")
for item, price in prices.items():
    print(f"{item:<10} : Tk {price:.2f}")

order = {}
n = int(input("\nHow many order entries? "))

for i in range(1, n + 1):
    item = input(f"Enter product {i}: ").strip().lower()
    qty = int(input("Enter quantity: "))

    if item not in prices:
        print(f"{item} is not available.")
    elif qty <= 0:
        print("Quantity must be positive.")
    else:
        order[item] = order.get(item, 0) + qty

print("\nFinal order:")
print(order)

bill = {}
for item, qty in order.items():
    bill[item] = {"quantity": qty,
        "unit_price": prices[item],
        "total": qty * prices[item]}
    
subtotal = sum(info["total"] for info in bill.values())
discount = subtotal * 0.05 if subtotal >= 1000 else 0.0

vat = 0.02 * (subtotal - discount)
final_amount = subtotal - discount + vat

print("\n================ GROCERY SHOP BILL ================")
print(f"{'Item':<10} {'Quantity':>8} {'Unit Price':>12} {'Total':>10}")
print("-" * 52)


for item, info in bill.items():
    print(f"{item:<10} {info['quantity']:>8} {info['unit_price']:>12.2f} {info['total']:>10.2f}")
print("-" * 52)
print(f"Subtotal:      Tk {subtotal:.2f}")
print(f"Discount (5%): Tk {discount:.2f}")
print(f"VAT (2%):      Tk {vat:.2f}")
print("-" * 52)
print(f"Final amount:  Tk {final_amount:.2f}")
print("=" * 52)