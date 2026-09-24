def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
n = int(input("enter number: "))
result = factorial(n)
print("Factorial: " , result)

def power(a,n):
    if n==0:
        return 1
    else:
        return a*power(a,n-1)
a = int(input("Enter number: "))
n = int(input("Enter power: "))
result = power(a,n)
print(f"the power of {a} is ", result )

def sum_num(n):
    if n == 0:
        return 0
    else:
        return n + sum_num(n-1)
n = int(input("enter the value: "))
result = sum_num(n)
print("sum of n: " , result)