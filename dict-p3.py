stock = {"pen": 12, "book": 3, "bag": 2,
         "ruler": 9, "calculator": 1}
x={ }
count=0
for i,j in stock.items():
  count=count+j
  if j <5:
    x[i]=j #in new dictionary products are added in this way
    
    
print("Total units: ",count)
print("Low stock:",x)