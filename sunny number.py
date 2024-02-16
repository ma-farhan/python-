n=int(input("enter a num:"))
temp=n
n=n+1
sq=n**0.5
if n%sq==0:
  print(temp,"is a sunny number")
else:
  print(temp,"is not a sunny number")