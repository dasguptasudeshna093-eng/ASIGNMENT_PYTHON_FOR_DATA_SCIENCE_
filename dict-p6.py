marks = [88, 74, 93, -5, 61, 47, 105, 82, 59]
valid=[]
grade={"A":0,"B":0,"C":0,"F":0}

for i in marks:
  if i>=0 and i<=100:
    valid.append(i)

for i in valid:
  if i>=80:
    grade["A"]+=1
  elif i<80 and i>=70:
    grade["B"]+=1
  elif i<70 and i>=60:
    grade["C"]+=1
  else:
    grade["F"]+=1
x=sum(valid)/len(valid)

print("Valid Marks: ", valid)
print ("GRADES: ",grade)
print("Average Marks: ",x)