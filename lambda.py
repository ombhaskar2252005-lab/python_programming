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