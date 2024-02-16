#4.REVERSE OF A NUMBER

num = input("Enter the first number:")
string=str(num)
reverse = ""
for i in num:
   reverse = i+reverse
print('The reverse number is =', reverse)