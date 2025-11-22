

student = {"rollno ":1, "name":"Anil" , }
print(type(student))
print(student)

student["city "] = "Indore"   #new add
student["rollno "]= 2         #update value
print(student)


student.update({"value ":5})
print(student)

print(student.keys())
print(student.values())
print(student.items())


student.pop("city")
print(student)

student.popitem(2)
print(student)


