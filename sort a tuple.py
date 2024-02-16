# 8.sort a tuple

t = (3,2,7,4)
t=list(t)
for i in range(0, len(t)):
    for j in range(i+1, len(t)):
        if t[i] >= t[j]:
            t[i], t[j] = t[j],t[i]
t=tuple(t)
print(t)