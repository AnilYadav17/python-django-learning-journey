#prg for create a class 

class product:
    def setvalue(self, x,y):
        self.code= x
        self.name = y
    def display(self):
        print("Code =", self.code)
        print("Name =", self.name)

obj = product()
obj.setvalue()
obj.display()
