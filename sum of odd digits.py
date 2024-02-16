num = int(input("Enter a series of numbers: "))
odd = 0
while num > 0:
    digit = num % 10
    if(digit%2 == 1):
        odd += digit
    num = num//10
print("Sum of odd digits: ", odd)