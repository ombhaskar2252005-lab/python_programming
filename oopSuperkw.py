'''We use the super keyword to access the same name method or when both parents and child
class have conctructor without super keyword the parents class constructor does not work'''
# for the same name method
class parent:
    def show(self):
        print("It is the parent class.")
class child(parent):
    def show(self):
        super().show()
        print("It is the child class.")
c = child()
c.show()
# for the constructor
class phone:
    def __init__(self,brand,ram,price):
        print("Inside the parent class")
        self.brand = brand
        self.ram = ram
        self.price = price
class smartphone(phone):
    def __init__(self,brand,ram,price,os,camera):
        print("Inside the child class")
        super().__init__(brand,ram,price)
        self.os = os
        self.camera = camera
s = smartphone("Apple",4,90000,'IOS','12px')  
print(s.brand)
print(s.camera)
print(s.price)     
