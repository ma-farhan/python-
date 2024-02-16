n=int(input("enter a num:"))
temp=n
for i in range(0,n+1):
  digit=n%10
  if digit==7 or n%7==0:
    print(temp,"buzz")
    break
else:
  print(temp,"not buzz")