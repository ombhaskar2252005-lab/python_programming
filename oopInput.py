# Taking input outside the class
class student:
    def __init__(self,name,age,standard):
        self.name = name
        self.age = age
        self.standard = standard
name = input("Enter the name: ")
age = int(input("Enter the age: "))
standard = input("Enter the class: ")
s = student(name,age,standard)
print("Student Details: ")
print("Student name is:",s.name)
print(s.standard)
print(s.age)
# Taking input inside the class
class employee:
    def __init__(self):
        self.name = input("Enter the name: ")
        self.age = int(input("Enter the age: "))
    def display(self):
        print("Nmae:",self.name)
        print("Age:",self.age)
# creating two object
e1 = employee()
e2 = employee()
print("Employee 1: ")
e1.display()
print("Employee 2: ")
e2.display()

#taking input outside the class for the two object
class car:

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def display(self):
        print("Name:", self.name)
        print("Speed:", self.speed)


# Taking input outside the class
name1 = input("Enter first car name: ")
speed1 = int(input("Enter first car speed: "))

name2 = input("Enter second car name: ")
speed2 = int(input("Enter second car speed: "))


# Creating two objects
c1 = car(name1, speed1)
c2 = car(name2, speed2)


# Displaying information
print("Car 1:")
c1.display()

print("Car 2:")
c2.display()