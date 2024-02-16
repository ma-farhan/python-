# 9.count the number of occurences of item 50 from a tuple

t=(3,50,30,50,50,78)
list1=list(t)
item=50
c=0
for k in list1:
  if item==k:
     c+=1
print(item,"occured",c,"times")

l=tuple(list1)
print(l)