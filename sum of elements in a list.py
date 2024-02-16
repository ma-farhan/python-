# 6..sum of elements in a list

lst = []
sum = 0
ele = int(input('How many numbers: '))

for i in range(ele):
    n = int(input('Enter number '))
    lst.append(n)

for j in range(0, len(lst)):
    sum = sum + lst[j]

print("sum is :", sum)