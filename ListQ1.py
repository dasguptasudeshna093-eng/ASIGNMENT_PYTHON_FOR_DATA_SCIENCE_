
values = [12, -5, 0, 7, -3, 0, 18, -1]
positive_values= []
negative_values= []
zero_values= []

for num in values:
    if num > 0:
        positive_values.append(num)
    elif num < 0:
        negative_values.append(num)
    else:
        zero_values.append(num)

print("Positive: ", positive_values)
print("Negative: ", negative_values)
print("Zero: ", zero_values)
print("Count: ", len(positive_values), len(negative_values), len(zero_values))
