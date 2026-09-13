#MAP
numbers = [1,2,5,6]
result = map(str,numbers)
print(list(result))

num = input().split()
# Convert each element to string
string_list = list(map(str, num))
# Convert each element to integer
int_list = list(map(int, num))
print(string_list)
print(int_list)

def cube(x):
    return x*x*x
# print(cube(2))
l = [2,4,8,7]
newl = list(map(cube,l))
print(newl)
print()

#filter
def avg(a,b,c):
    return a+b+(c/3)
num3 = [1,2,5,8]
result = list(filter(lambda x: x % 2 == 0, num3))
print(result)
print(avg(1,7,8))

num2 = [2,9,6,8,7]
def even(x):
    return x%2==0
result = list(filter(lambda x: x%2==0, num2))
print(result)
print()

avg1 = lambda x,y,z:(x+y+z)/3
print(avg1(2,5,8))