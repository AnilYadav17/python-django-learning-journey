#serching in the list 

lst = [10, 11, 14, 15, 82, 45, 25]
print(lst)

search = int(input("Enter data to be search :"))
temp = 0

for i in range(0, len(lst)):
    if lst[i] == search:
        temp=1 #data found
        break

if temp == 1:
    print("Element found")
else:
    print("Element not found")