#   prg for dynamic dict

student = {}   #empty dictionary

n = int(input("Enter the limit :"))
for i in range(0 , n):
    key = input("Enter the key : ")
    data = input("Enter the value : ")
    student.update({key:data})

print(student)

