#program for dynamic list

lst = []

n = int(input("Enter the limit :"))
for i in range(0,n):
    data = int(input("Enter value : "))
    lst.append(data)

print(lst)