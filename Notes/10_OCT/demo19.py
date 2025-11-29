#prog for display division

per = float(input("Enter your percentage : "))
if per>85:
    print("I Division ")
elif per>60 and per<85:
    print("II Division")
elif per>45 and per<60:
    print("III Division")
else:
    print("FAIL !")