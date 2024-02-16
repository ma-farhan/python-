n=int(input("enter a num:"))
temp=n
sum=0
total=0
while n>0:
  digit=n%10
  sum+=digit
  n//=10
while sum>0:
  d=sum%10
  total+=d
  sum//=10
print(total)
if total==1:
  print(temp,"is a magic number")
else:
  print(temp,"is not a magic number")