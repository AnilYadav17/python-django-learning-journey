#prg for create a class 

class product:
    def setvalue(self):
        self.code=101
        self.name = "mobile"
    def display(self):
        print("Code =", self.code)
        print("Name =", self.name)

obj = product()
obj.setvalue()
obj.display()
