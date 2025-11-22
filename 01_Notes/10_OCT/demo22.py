#factorial or given number

n = int(input("Enter any number :"))
a = 1 
f = 1 

while a<=n:
    f = f*a
    a+=1 
print("Factorial = ", f)