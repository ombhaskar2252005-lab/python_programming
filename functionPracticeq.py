print("Function practice question")
# 1. greet method
# def greet(name):
#     print("hello ",name)
# name = input("Enter a name: ")
# greet(name)

# 2. even or odd
# def typeofnum(number):
#     if number%2 ==0:
#         print("even")
#     else:
#         print("odd")
# number = int(input("enter the number: "))
# typeofnum(number)

# 3. maximum number
# def max(num1, num2):
#     if num1>num2:
#         print(num1, " is maximum number.")
#     else:
#         print(num2, " is maximum.")
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# max(num1,num2)

# 4.factorial
# def factorial(n):
#     fact =1
#     for i in range(1,n+1):
#         fact = fact * i
#     print("Factorial: ", fact)
# n = int(input("Enter a number: "))
# factorial(n)

# 5.prime number
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i ==0:
#             return False

#     return True

# n = int(input("Enter number: "))
# if is_prime(n):
#     print("prime number")
# else:
#     print("not prime number")

# 6. average of list
# def avglist(numbers):
#     total =0
#     for num in numbers:
#         total += num
#     return total/len(numbers)
# numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
# print("Average:", avglist(numbers))

# 7. calculator with operator
# def calculator(a,b,op):
#     if op == "+":
#         return a+b
#     elif op == "-":
#         return a-b
#     elif op == "*":
#         return a*b
#     elif op == "/":
#         if b == 0:
#             return "Cannot divide"
#         return a/b
#     else:
#         return "Invalid operator"

# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# op = input("Enter operator (+,-,*,/): ")
# print("Result: " , calculator(a,b,op))

# 8. even number in list will print
# def evennum(num): 
#   result = []
#   for n in num:
#     if n % 2 == 0:
#       result.append(n)
#   return result 
  
# num = list(map(int,input().split()))
# print(evennum(num))

# 9. even number between the two number
def even(num):
    if num % 2 ==0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

n = int(input("Enter 1st integer: "))
m = int(input("Enter 2nd Integer: "))
for i in range(n,m):
    even(i)

print()
# *args function
print("args function")
def add(*args):
    total =0
    for i in args:
        total = total + i
    return total
print("Sum:",add(1,2,2,3,4,5)) #method call

print()

def multiply(*number):
    product =1
    for i in number:
        product = product *i
    print("Product:",product)
multiply(1,2,3,4,5)

# **kwargs function
print()
print("Kwargs function")

def show(**kwargs):
    print(kwargs)
show(name = "Rahul", age = 19)

def capital(**country):
    for(key,value) in country.items():
        print(key, ':', value)
capital(India = 'Delhi', Nepal = 'Kathmandu')

#nested function
def f():
    def g():
        print("inside function g")
    g() #function call
    print("inside function f")
f()
# function is a data type in python
def square(num):
    return num**2
print(type(square))
print(square(4))
