#extend

lst1 = [1, 3, 5, 4, 5]
lst2 = [8, 9, 5, 6, 3]

print("List 1 :", lst1)
print("List 2 :", lst2)

lst1.extend(lst2)
print("List1 Extend :", lst1)

lst2.extend(lst1)
print("List2 Extend :", lst2)
