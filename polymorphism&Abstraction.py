
# Polymorphism 
# 1. method overriding
class animal:
    def sound(self):
        print("Animal makes sound")
class dog(animal):
    def sound(self):
        print("dogs barks")
class cat(animal):
    def sound(self):
        print("cat meows")
a = animal()
a.sound()        
d = dog()
d.sound()
c = cat()
c.sound()
# 2. duck typing
# it doesnot require inheritance
class dog:
    def show(self):
        print("It is a dog.")
class cat:
    def show(self):
        print("It is a cat.")
def let_see(obj):
    obj.show()
d = dog()
c = cat()
let_see(d)
let_see(c)
# 3. operator overloading
class A:
    def __init__(self,value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value
a = A(20)
b = A(10)
print(a+b)
# 4. Method Overloading
# it doesnot work like java in python it have different way
class calculator:
    def add(self, *args):
        print(sum(args))
obj = calculator()
obj.add(10,20)
obj.add(70,21,4)

#Abatraction
from abc import ABC, abstractclassmethod
class BankApp(ABC):
    def database(self):
        print('Connected to database')
        @abstractclassmethod
        def security(self):
            pass
class MobileApp(BankApp):
    def security(self):
        print("Mobile secure")
m = MobileApp()
m.security()
     