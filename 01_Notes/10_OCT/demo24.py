#1!+2!+3!+....
n = int(input("Enter Step :"))
a = 1
s = 0
f = 1

while a<=n:
    f = f *a 
    print("Factorial =", f)
    s = s+f
    a += 1
print("Sum :", s)