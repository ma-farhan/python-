#2.BIGGEST DIGIT OF A GIVEN NUMBER

number = int(input("Enter a number: "))
string = str(number)
maximum= 0
for i in string:
    store_i = int(i)
    if store_i > maximum:
        maximum = store_i
print("The biggest digit : ",maximum)