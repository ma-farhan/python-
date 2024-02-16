# 5.Find the index of a specific element in a list

lst=[]
limit=int(input("enter the limit:"))
for i in range(limit):
  num=int(input())
  lst.append(num)
print(lst)
ele=int(input("enter a element:"))
for i in range(limit):
  if ele==lst[i]:
    index=i
print("the index is:",index)