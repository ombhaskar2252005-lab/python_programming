student= {"name": "bhaskar", "age": 20, 102:"roll no"}
# toh yahan name age 102 key ha
print(student)
print(student["name"])
print(student[102])
print(type(student))
print(student.keys())
#taking input
#1. when the keys are given and we want to int or other input
animal ={} #empty dictionary
animal["name"] = input("Enter the name: ")
animal["age"] = int(input("Enter the age: "))
animal["sound"] = input("Enter sound: ")
print(animal)
# 2. we use it when we have to take key and value both as input but in this integer is taken as string input
n= int(input("Enter number of items: "))
employee = {}
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    employee[key] = value
print(employee)

