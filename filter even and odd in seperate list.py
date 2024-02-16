# 2..filter even and odd numbers in a separate list

lst=[]
num=int(input("Enter number of elements:"))
for i in range(1,num+1):
    ele=int(input("Enter elements:"))
    lst.append(ele)
even=[]
odd=[]
for j in lst:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("The even list",even)
print("The odd list",odd)
