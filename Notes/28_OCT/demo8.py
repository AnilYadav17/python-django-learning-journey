# s1 = set((1, 22, 35, 4, 6,6, 7, 8))
# print(type(s1))
# print(s1)

#prg for dynamic set creation
s1 = set(())
n = int(input("Enter the limit"))
for i in range(0, n):
    data = int(input("Enter the data:"))
    s1.add(data)
    s1.remove(2)
print(s1)