# fibonacci

limit=int(input("enter a num:"))
a=0
b=1
print(a)
print(b)
sum=0
for i in range(0,limit-2):
  temp=a
  a=b
  b=temp+a
  print(b)