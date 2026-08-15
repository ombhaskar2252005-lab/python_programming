#list
fruits = ["apple", "banana", "cherry"]
#append - used to add element at last
fruits.append("orange")
print(fruits)
#insert - used to add element at specific index
fruits.insert(1,"strawberry")
print(fruits)
#remove- used to remove element from list
fruits.remove("banana")
print(fruits)
fruits.pop(2) #removes element at index 2
print(fruits)
#len - used to find length of list
print(len(fruits))

#tuples
point = (3,4)
x,y=point
print(x,y)
#tuple is unchangeable
#dictionaries
students = {"name":"john", "age":21,
            "course":"python"}
print(students["name"])
students["age"]=22 #update value
print(students)
#sets
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a.union(b)) #prints all elements from both sets
print(a.intersection(b)) #prints common elements from both sets
print(a-b) #prints elements in a but not in b
#ternary
print("hot" if 30>20 else"cold")
#common built in exceptions
#valueError right type wrong value e.g int("hello")
#typeError wrong type of argument passed to a function
#indexError index out of bound or range
#keyerror dictionary key doesn't exist
#zeroDivisionError in this int is divided by zero
