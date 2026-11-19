class User:
    def __init__(self):
        self.name = "sumi"
        self.gender = 'female'
    def login(self):
        print("Please login")
class student(User):
    def enroll(self):
        print("enroll in any course")
u = User()
s = student()
print(s.name)
print(s.gender)
s.login() #child can access the parent class object
s.enroll()

"""so as we know child class can inherite the parent constrtuctor and use it when 
child class doesnot have constructor but when child class have constructor and parents 
class also have then the parents class will not initialize or execute """ 
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, os, ram):
        self.os = os
        self.ram = ram
        print ("Inside SmartPhone constructor")
    def display(self):
        print(self.os,self.ram)

s=SmartPhone("Android", 2)
#print(s.brand) this will show error because brand is in parents constructor and it does not get initialize
s.display()
print(s.os)
print(s.ram)

#child class vs private attributes/methods
class phone:
    def __init__(self,brand,price):
        print("Inside the parents constructor")
        self.brand = brand
        self.__price = price #private krdiye price ko

    # we use getter to access the private attributes
    def show(self):
        print(self.__price)

class smartphone(phone):
    def check(self):
        print(self.__price)

sp = smartphone("Apple", 909090)
# sp.check() this will show error
sp.show()
print(sp.brand)