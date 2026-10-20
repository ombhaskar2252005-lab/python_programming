#write a python program to print your name
#write a python program to add, subtract and multiply 2 number
print("My name is Bhaskar")
a = 10
b = 5
print("Addition: " , a+b)
print("Subtract: ", a-b)
print("Multiply: " , a*b)
# g = int(input("Enter a number: "))
# j = int(input("Enter 2nd number: "))
# subtract = g - j
# print(subtract)
#tuple 
tup = 1,3
print(type(tup))
tup1 = 1, # , se tuple type ho jata ha
print(type(tup1))
x = int("20",4)
print(x)
a = int(input())
b = int(input())
c = int(input())
print(f"Greater or equal to {c}: ")
for i in range (a, b+1):
    if (i>=c):
        print(i)
print(f"less than {c}: ")
for i in range(a,b+1):
    if(i<c):
        print(i)