# 1. single inheritance toh jante hi ho
# 2. Multilevel Inheritance
class product:
    def review(self):
        print("The product is good")

class phone(product):
    def __init__(self,name,price,ram):
        print("Inside the phone class")
        self.name = name
        self.price = price
        self.ram = ram

class smartphone(phone):
    def show(self):
        print("child class")

s = smartphone("apple", 30000,4)
print(s.name)
s.review()
s.show()

# 3. Multiple inheritance
#input leke hai
class phone:
    def __init__(self,brand,price,camera):
        print("Parent class")
        self.brand = brand 
        self.price = price
        self.camera = camera
    def buy(self):
        print('Buying the phone')
class product:
    def show(self):
        print("Customer review")
class smartphone(phone,product):
    pass
brand = input("Enter the brand name: ")
price = int(input("Enter the price: "))
camera = input("Enter the pixel: ")
s = smartphone(brand,price,camera)
s.buy()
s.show()
print(s.brand)
print(s.price)
print(s.camera)

# 4. Hierarchical inheritance
class parent:
    def __init__(self,title,income):
        print("Parent class")
        self.title = title
        self.income = income
class child1(parent):
    pass
class child2(parent):
    pass
title = input("Enter the title: ")
income = int(input("Enter the income: "))
c1 = child1(title,income)
c2 = child2(title,income)
print(c1.income)
print(c2.title)