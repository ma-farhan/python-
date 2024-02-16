num=int(input("enter a number:"))
sum=0
product=1
while num!=0:
  digit=num%10
  sum+=digit
  product*=digit
  num//=10
if sum==product:
  print("spy number")
else:
  print("not a spy number")