##LIST -> MUTABLE AND ORDERED THAT ALLOWS DUPLICITY 
lst1 = [1,2,3,4.5]
lst1.append(10)
print("LIST :\n",lst1)
lst1.pop()
print(lst1)
lst1.insert(0, 1)
print(lst1)
lst2 = [1, 2, 3, 4]
lst1.extend(lst2)
print(lst1)
lst1.sort()
print(lst1)
lst1.reverse()
print(lst1)
lst3 = set(lst1)
lst3 = list(lst3)
print(lst3)




##TUPLE -> COLLECTION OF UNORDERED , UNMUTABLE , HETEROGENOUS AND ALLOWS DUPLICITY
tpl1 = ()
print("\n\n\n","TUPLES :\n", type(tpl1))
tpl1 = (1,1, 1, 1, 1, 2,3,"Anil")
print("Tuple1 :", tpl1)
print("Index of Anil :", tpl1.index("Anil"))
print("Count of 1 :", tpl1.count(1))
print(tpl1)
tpl2 = set(tpl1)
print(tpl2)
tpl3 = tuple(tpl2)
print(tpl3)





##SET -> UNOERDERED , MUTABLE WITH NOT DUPLCATE ELEMENTS IN IT 
print("\n\n\n\n\n\n\nSET:")
set1 = {1, 3 ,3 }
print(set1)
set1.add(2)
print(set1)
set1.update([2, 5, 6, 7, 8, 2, 3, 1, 5, 4, 0, 5, 8])
print(set1)
set1.pop()
print(set1)





##Dictionary -> 
dist1 = {1:2, 2:3}
print("\n\n Dictionary :\n",type(dist1))
dict1 = dict()
print(dict1)
dict1.update({1:0, 2:0})
print(dict1)
print(dist1)
print(dist1[1])
for key in dict1:
    print("Key :", key , "\nValue: ", dict1[key])
print("Value for key 1 :", dict1[1])