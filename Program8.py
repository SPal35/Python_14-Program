list1 = [1, 3, 6, 78, 35,55]
print("First list is:", list1)
list2 = [12, 24, 35, 24, 88, 120, 155]
print("Second list is:", list2)
newList = []
for element in list1:
    if element in list2:
        newList.append(element)
print("Intersection of the lists is:", newList)