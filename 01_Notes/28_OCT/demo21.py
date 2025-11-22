#parameterized constructor
class product:
    def __init__ (self, qty , price):
        self.total= qty*price
        print("Total Price :", self.total)



obj = product(65, 25)
obj.product(10, 20)
obj.product(10, 20, 30)