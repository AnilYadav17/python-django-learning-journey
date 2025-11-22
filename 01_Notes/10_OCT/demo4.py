import sys

a = 5.4 
print("a = ", a, type(a))
print("Size :", sys.getsizeof(a), "bytes")



# b = "abc"   {49+1+1+}
b = "abc"
print("b = ", b, type(b))
print("Size :", sys.getsizeof(b), "bytes")

c = False
print("c = ", c, type(c))
print("Size :", sys.getsizeof(c), "bytes")

d = None
print("d = ", d, type(d))
print("Size :", sys.getsizeof(d), "bytes")

