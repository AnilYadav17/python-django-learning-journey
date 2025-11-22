# # from module1 import a, b
# # def sum():
# # 	return a+b

# # print("Sum : ", sum())

# # from module1 import a,b

# # def mul(a,b):
# #     return a*b

# # print("Multiplication : ", mul(a,b))

# # from module1 import a
# # def demo(*a):
# #     print("*a : ", a)
# #     print("Type : ", type(a))

# # demo()


# from module1 import a,b

# # def sum():
# #     c= a+b
# #     print("Sum :", c)

# # sum()

# # def sum():
# #  return a+b

# # print("Sum with return :", sum())
# # sum()

# # def add(*numbers):
# #     print(sum(numbers))

# # add(2, 3, 4, 5)


# # def sum(*numbers):
# #     print(sum(numbers))

# # numbers = 1,2,2, 3

# # sum()


# # def add_all(*a):
# #   print("Type :", type(a))
# #   total = 0
# #   for i in a:
# #    total += i
# #   return total 
# # print("Sum :", add_all(10,20,30.4))


# def findall(**a):
#     print(type(a), a)

# findall(a=10, b="Anil")



    

# from module1 import a,b

# for i in range(1, a+1 ,1):
#    print(i)


# a = 10
# b = 10.57767
# print(type(str(a)))
# print(type(int(b)))


# #-----> LIST <---------
# lst = [1, "Anil ", "YAdav0", 17.171717]
# lst1  = [1, 2, 3 ,4]
# print(type(lst))
# for i in lst:
#     print(i)

# lst.append(10)
# print(lst)

# lst1.insert(4,5)
# print(lst1)

# lst1.remove(5)
# print(lst1)

# lst1.pop(3)
# print(lst1)

# lst1.extend([0,1])
# print(lst1)

# lst1.sort()
# print(lst1)

# lst1.sort(reverse=True)
# print(lst1)

# print("Count of 1 :" , lst1.count(1))

# print("Index of 2 :", lst1.index(2))

# print(lst1.clear())
# print(lst1)


#-------->TUPLE <------------
# tpl = ("Anil", 20 , 30)
# tpl1 = (10)
# print(type(tpl1))

# tpl2 = (20,)
# print(type(tpl2))

# print(tpl)
# print(type(tpl))

# for i in tpl:
#     print(i)
#     print(type(i))

# print(tpl.count(20))
# print(tpl.index(20))


#-----------> SET <---------
# ...existing code...

# s = set()   # create empty set
# s.add(1)    # add 1
# print(s)    # {1}

# s1 = s
# s1.add(12)
# print(s1)# create
# s = set()          # empty
# s = {1, 2, 3}

# # add / update
# s.add(4)           # single element
# s.update([5, 6])   # add many from an iterable
# # s is now {1,2,3,4,5,6}

# # remove vs discard
# s.remove(6)        # removes 6, raises KeyError if missing
# s.discard(10)      # removes 10 if present, no error if not

# # pop (removes and returns an arbitrary element)
# x = s.pop()

s1 = set()
s1.add(4)
s1.update([1,3])
s1.update([2,44])
print(s1)
s1.clear()
print(s1)
s1.update([2, 4 ,5 ,6 ,7 ,8])
print(s1)
print(type(s1))

s2 = s1.copy()
s2.update([10, 20, 30, 40, 50])
print(s2)

print("Union :", s1.union(s2))
print("Intersection :", s1.intersection(s2))
print("Difference :", s1.difference(s2))

s3 = {1, 3 , 5 ,7 }
s4 = {5, 7 , 8 ,9 }

print(s3 ,"\n", s4)
print("Union :", s3|s4)
print("Intersection :", s3&s4)
print("Difference ", s3-s4)
print("Assymetric Diff. :", s3^s4)

print(s3.union(s4))

