
numbers = [4, 7, 2, 7, 9, 7, 1]
target = 7
positions = []

for index, num in enumerate(numbers):
    if num == target:
        positions.append(index)

print("Target:", target)
print("Positions:", positions)
print("Number of occurrences:", len(positions))

first = -1

for index, num in enumerate(numbers):
    if num == target:
        first = index
        break
if first != -1:
    print("First occurrence:", first)
else:
    print("Target not found")
