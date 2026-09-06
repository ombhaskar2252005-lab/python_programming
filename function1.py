def greet(name):
    print("hello, " + name)
greet("sumi")

def suyashgandu():
    pass  #ye pass likhne se function ko empty chhod sakte hain or baad me usme likh shakte ha ye error nahi dega

def add(a=3,b=6):
    print(a+b)
    # print(type(add))
add(a=9,b=5) #default value of a is 3 and b is 5 so output will be 8


def greaternum(a,b):
    if(a>b):
        print(a, "is greater")
    else:
        print(b, "is greater")
a = int(input("enter first number: "))
b = int(input("enter second number: "))
greaternum(a,b)


def name(fname, mname, lname):
    print("Hello " + fname + " " + mname + " " + lname)
name(lname = "Sharma", mname = "kumar", fname = "Ravi") #not necessary to follow the order of parameters if we use keyword arguments


def average(num1, num2):
    return (num1+num2)/2
num1 = int(input("Enter a number: "))
num2 = int(input("Enter 2nd number: "))
result = average(num1, num2)
print(result)