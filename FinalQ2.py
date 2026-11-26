n=int(input("Enter a number: "))
sum=0
i=1
count_odd=0
sum1=0
sum2=0
for i in range(i,n+1):
  if i>0:
    sum2=sum2+i
    if i%2==0:
         sum=sum+i
    elif i%2!=0:
         count_odd=count_odd+1
    elif i%3==0 and i%5==0:
         sum1=sum1+i
       
  else:
    print("Invalid number")

print("Sum of even numbers= ",sum)
print("Odd numbers= ",count_odd)
print("Sum of the numbers divisible by 3,5= ",sum1)
print("Average of all integers= ",sum2/n)