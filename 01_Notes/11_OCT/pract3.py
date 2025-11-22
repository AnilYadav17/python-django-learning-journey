##Strings
print("String: ")
Str = "This is a Testing String "
print(Str.upper())
print(Str.lower())
print(Str.capitalize())
print(Str.count("This"))
Str1 = "Anil Yadav "
Str2 = Str1+Str
print(Str2)
print(Str*1)
result = "This" in Str
print("IS THIS presend in Str :", result)
not_result = "Hii " not in  Str
print("IS HII  not present in Str :", not_result)

print(Str.isalpha(), Str.isupper(), Str.isprintable())
