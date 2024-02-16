# 4.merge two sorted list to form a sorted list

list1 = [3,2,6,1]
for i in range(0, len(list1)):
    for j in range(i+1, len(list1)):
        if list1[i] >= list1[j]:
            list1[i], list1[j] = list1[j],list1[i]
list2= [4,7,2,4]
for i in range(0, len(list2)):
    for j in range(i+1, len(list2)):
        if list2[i] >= list2[j]:
            list2[i], list2[j] = list2[j],list2[i]
sorted_list =[]
sorted_list += list1
sorted_list += list2
print(sorted_list)