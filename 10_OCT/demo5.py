s1 = "This is a test program! "
# search = "test"
# result = search in s1

result = "test" in s1
print(result, ", Type :", type(result))

result = "xyz" in s1
print(result, ", Type :", type(result))

result = "xyz" not in s1
print(result, ", Type :", type(result))