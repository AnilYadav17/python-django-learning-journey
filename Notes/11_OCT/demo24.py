#program for create a tuple 

t1 = (51, 25, 13, 44 )
print(t1)
print(type(t1))

#convert to list
list1 = list(t1)

list1.append(100)
print(list1)

list1.insert(1, 20)
print(list1)

list1.pop()
print(list1)

list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

#convert to tuple
t2 = tuple(list1)
print(t2)