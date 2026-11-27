prices = {"pen": 15, "book": 120, "bag": 850}
requested_items = ["book", "ruler", "pen"]


for i in requested_items:
  if i in prices:
    print(i,': tk',prices.get(i))
  else:
    print(i,':',"not found")