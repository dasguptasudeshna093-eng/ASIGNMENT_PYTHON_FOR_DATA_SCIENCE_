number=int(input("Give your number:- "))

if 0<=number<=100:
    if 80<=number<=100:
      print("A")
    elif 70<=number<=79:
      print("B")
    elif 60<=number<=69:
      print("C")
    elif 50<=number<=59:
      print("D")
    else:
      print("F")
else:
  print("Invalid marks")

if number>=50:
  print("Pass")
else:
  print("Fail")