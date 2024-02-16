n=int(input("enter a num:"))
temp=n
sum=0
sq=temp*temp
print(sq)
while sq>0:
  digit=sq%10
  sum+=digit
  sq//=10
print(sum)
if temp==sum:
  print(temp,"is a neon number")
else:
  print(temp,"is not a neon number")