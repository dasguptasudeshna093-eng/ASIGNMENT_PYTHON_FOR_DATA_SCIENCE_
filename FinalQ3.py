numbers = [12, 7, -4, 12, 18, 5, -3, 8, 18]
non_negative_numbers = [ ]
unique=[]
count_negative=0
for number in numbers:
  if number>0:
    non_negative_numbers.append(number)
  else:
    count_negative=count_negative+1

for num in non_negative_numbers:
  if num not in unique:
    unique.append(num)
  else:
    continue
x=numbers[1:9:2]


print("NON-NEGATIVE NUMBERS: ",non_negative_numbers)
print("UNIQUE NUMBERS: ",unique)

print("Sum of all non-negatives ",sum(non_negative_numbers))
print("Total negative numbers: ",count_negative)
print(x)
