lst1 = [1, 5, 3, 7, 8, 9]
print("List before sort :", lst1)
n = len(lst1)

a = lst1


# for i in range(0, n):
#         for j in range(0, n - 1):
#             if lst1[j] > lst1[j + 1]:
#                 lst1[j], lst1[j + 1] = lst1[j + 1], lst1[j]

for i in range(0, n):
    for j in range(0, n-i-1):
        if a[j]>a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print("After sort : ",a)  # Output: [1, 3, 5, 7, 8, 9]