n=int(input("enter a num:"))
for i in range(1,n):
  if i*(i+1)==n:
    print(i,i+1)
    print(n,"is a pronic number")
    break
else:
  print(n,"is not a pronic number")