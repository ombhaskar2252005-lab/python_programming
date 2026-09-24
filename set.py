s = {23,45,56,23,"Om",1.23,True}
print(s) #set is unordered
numbers = set(map(int,input("Enter value: ").split()))
print(numbers)
harry = set() #creating empty set
print(type(harry))

#to access element in set we use for loop
for i in s:
    print(i) 

#methods in sets
print()
ele = {2,4,22}
# ele.add(3)
# print(ele)
ele.remove(2)
print(ele)
ele.clear()
print(ele)
a = {1,3,5,6}
b={1,2,4,6}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
c = {2,3,4,8}
d = {2,8}
print(d.issubset(c))
print(c.isdisjoint(d))
e = {2,3}
f = {4,6}
# print(e.update(f)) this does not work here
e.update(f)
print(e) 
# intersection_update, difference_update, symmetric_difference_update ye sab ko bhi update ke tarah likhte h