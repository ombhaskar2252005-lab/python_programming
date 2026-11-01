a = lambda x,y: x+y
print(a(2,4))

#check if 's' is present in string
string = lambda a: 's' in a
print(string('hello'))

# lambda with map function
number = [1,2,3,4,5]
num = list(map(lambda x:x**2, number))
print(num)

# lambda with filter function
l = [12,22,36,78,33]
filtered = list(filter(lambda x:x>32, l))
print(filtered)

fruits = ['apple', 'banana', 'cherry', 'kiwi']
name = list(filter(lambda x:x.startswith('a'), fruits))
print(name)

# lambda with reduce function
import functools
num1 = [1,4,5,6,7]
result = functools.reduce(lambda x,y: x+y, num1)
print(result)

max = functools.reduce(lambda x,y:x if x>y else y, [23,45,67,69,0])
print(max)


price = float(input("Enter price: "))
discount_percent = float(input("Enter discount: "))
discount_value = lambda price,discount_percent: price-(price*(discount_percent/100))
print(discount_value(price,discount_percent))

time = int(input("ENTER time: "))
speed = int(input("enter speed: "))
distance = lambda time,speed: time*speed
print(distance(speed,time))



def sumoftwo(a,b=10):
    sum = a+b
    print(sum)
a = int(input("Enter a: "))
b = int(input("Enter b: "))
sumoftwo(a,b)
sumoftwo(a)