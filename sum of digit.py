num=int(input("enter a number:"))
sum=0
n=0
while num!=0:
  digit=num%10
  sum+=digit
  num//=10
single_digit=sum%10
n+=single_digit
print(n)