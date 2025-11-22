student = {"rollno ":1, "name":"Anil" , }
student["city "] = "Indore"   #new add
student["rollno "]= 2         #update value
print(student)

# x  =student.get("name")
# print(x)


studentnew = student.copy()
print(studentnew)

student.clear()
print(student)

del student
