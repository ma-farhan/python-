n=int(input("enter a num:"))
temp=n
st=str(n)
sum=0
pow=len(st)
while n>0:
  digit=n%10
  pos=digit**pow
  sum+=pos
  pow-=1
  n//=10
if temp==sum:
  print(temp,"is a disarium number")
else:
  print(temp,"is not a disarium number")