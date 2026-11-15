#basic code of oops
class student:
    def __init__(self): # default constructor
        self.name = "rahul"
        self.age = 20
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
s1 = student()
s1.gender = "male" #we can make variable outside the class but it is not a good practice
s1.display()
print(id(s1)) 

class car:
    def __init__(self,name,model):
        self.name = name
        self.model = model
name = input("Enter car name:")
model = input("Enter car model:")
c1 = car(name,model)
print(c1.name,c1.model)
c2 = car("BMW","X5")
print(c2.name,c2.model)

#parameterized constructor
class Faculty:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
f1 = Faculty("om",20)
f2 = Faculty("Ramesh",30)
f1.display()
f2.display()
print(id(f1))
print(id(f2))

print()
#special method __init__(),__str__(),__add__(),__sub__(),__mul__(),__truediv__() ye sab hote hai
class fraction:
    def __init__(self,x,y):
        self.num = x
        self.den = y
    def __str__(self): # display karne ke liye or It defines how an object should look when we print it.
        return '{}/{}'.format(self.num,self.den)
    def __add__(self,other):
        new_num= self.num*other.den + self.den*other.num
        new_den = self.den*other.den
        return '{}/{}'.format(new_num,new_den)
    def __sub__(self,other):
        new_num= self.num*other.den - self.den*other.num
        new_den = self.den*other.den
        return '{}/{}'.format(new_num,new_den)
    def __mul__(self,other):
        new_num = self.num*other.num
        new_den = self.den * other.den
        return '{}/{}'.format(new_num,new_den)
    def __truediv__(self,other):
        new_num = self.num*other.den
        new_den = self.den * other.num
        return '{}/{}'.format(new_num,new_den)
    def convert_to_decimal(self):
        return self.num/self.den
f1=fraction(2,3)
f2=fraction(3,4)
print(f1)
print(f2)
print(f1+f2) # '+' operator se __add__() method call hota hai
print(f1-f2) # '-' operator se __sub__() method call hota hai
print(f1*f2) # '*' operator se __mul__() method call hota hai
print(f1/f2) # '/' operator se __truediv__() method call hota hai
print(f1.convert_to_decimal())
