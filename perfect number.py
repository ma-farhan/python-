# perfect numbers

def Perfect(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            print(i)
            sum+=i
    if sum == n:
       print(n,"is a perfect number")
    else:
        print(n,"is not a perfect number")

n=int(input("Enter A number :"))
result=print(Perfect(n))