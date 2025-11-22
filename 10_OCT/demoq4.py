#fi nd max among three number using ladder if

num1=int(input("Enter first no :"))
num2=int(input("Enter second no : "))
num3=int(input("Enter third no :"))

if num1>num2 and num2>num3:
    print("Num 1 is greater ! ")
elif num2>num1 and num1>num3:
    print("Num 2 is greater !")
else:
    print("Num 3 id greater !")