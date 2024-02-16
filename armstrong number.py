#1.ARMSTRONG NUMBER

num = int(input("Enter a number to check : "))
string = str(num)
length = len(string)
sum = 0
for i in string:
    store_i = int(i)
    sum = sum+store_i ** length
if sum == num:
    print(sum,"is an armstrong number")
else:
    print(sum," is not an Armstrong number")