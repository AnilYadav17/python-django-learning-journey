#program for Variable length argument function

def demo(*a):
    print(a)
    print(type(a))

print(demo(10))
print(demo(1,4.5))

result1 = demo(1.5,4.5, 101)
print(result1)
