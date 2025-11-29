#prg for Distructor

#parameterized constructor
class product:
    def __init__ (self, qty , price):
        self.total= qty*price
        print("Total Price :", self.total)

    def __del__ (self):
        print("The Distructor ")


obj1 = product(65, 25)
obj2 = product(10, 20)
obj3 = product(10, 20)

obj1 = product()