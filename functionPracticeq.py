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
def calculator(a,b,op):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        if b == 0:
            return "Cannot divide"
        return a/b
    else:
        return "Invalid operator"

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
op = input("Enter operator (+,-,*,/): ")
print("Result: " , calculator(a,b,op))