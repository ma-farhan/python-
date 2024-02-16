n=int(input("enter a num:"))
temp=n
sum=0
total=0
while n>0:
  digit=n%10
  sum+=digit
  n//=10
print(sum)
if temp%sum==0:
  print(temp,"is a niven number")
else:
  print(temp,"is not a niven number")