# 1.prime numbers in given list

lst=[5,6,4,3,17,8]
l=len(lst)
for i in range(0,l):
  if lst[i]==1:
    continue
  for j in range(2,lst[i]):
    if lst[i]%j==0:
      break
  else:
      print(lst[i])