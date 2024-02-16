a=1
b=34
c=9
x=((b**2)-4*a*c)
if x==0:
  x1=(-b)/(2*a)
  print("solution is...",x1)
elif x>0:
  x2=(-b)+(x**(0.5))/(2*a)
  x3=(-b)-(x**(0.5))/(2*a)
  print("solution is...",x2,x3)
else:
  print("img")