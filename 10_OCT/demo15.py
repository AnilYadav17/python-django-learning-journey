#swapping o two 2 numbers withot using third number

a = 10 
b = 20 
print("Before swap :")
print("a = ", a)
print("b =", b)

print("After swap :")
a ^= b
b ^= a
a ^= b
print("a = ", a)
print("b =", b)



print("After swap :")
a, b = b , a 
print("a = ", a)
print("b =", b)


c = a 
a = b 
b = c
print("After swap :")
print("a = ", a)
print("b =", b)

print("After swap :")
a = a+b
b = a-b
a = a-b
print("a = ", a)
print("b =", b)