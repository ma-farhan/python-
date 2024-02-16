num1 = int(input("enter num1:"))
num2 = int(input("enter num2:"))
n=int(input("choose 1.add 2.sub 3.mul 4.div"))
if n==1:
  print("add:",num1+num2)
elif n==2:
  print("sub:",num1-num2)
elif n==3:
  print("mul:",num1*num2)
elif n==4:
  print("div:",num1/num2)
else :
  print("invalid")