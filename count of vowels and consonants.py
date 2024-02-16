a="pyEethon"
vowels=0
notvowels=0
for i in a:
  if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
    vowels+=1
  else:
    notvowels+=1
print("count of vowels,notvowels are:",vowels,notvowels)