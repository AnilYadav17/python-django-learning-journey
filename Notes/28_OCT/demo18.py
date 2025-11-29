#prg for create a class 

class product:
    def setvalue(self):
        self.code= int(input("Enter product code :"))
        self.name = input("Enter product name :")
    def display(self):
        print("Code =", self.code)
        print("Name =", self.name)

obj = product()
obj.setvalue()
obj.display()
