list1 = [1,4,6,7,8,15,7]
list2 = [2,5,7,18,25,15]

list3 = []
for i in list1:
    if i in list2 and i not in list3:
        list3.append(i)

print(list3)
        



    

