# 3.checking given sublist in a list

lst=[2,3,4,8,5]
sublst=[8,4]
for i in range(0,len(lst)):
  for j in range(0,len(sublst)):
    if lst[i]==sublst[j]:
      print(sublst[j],end=" ")
    else:
      continue
if lst[i]==sublst[j]:
      print(sublst[j],end=" ")