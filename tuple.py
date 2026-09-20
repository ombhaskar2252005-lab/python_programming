# tuple format
tup = (10,20,30,"green", False,10)
print(type(tup))
print("tuple is : " , tup)
print(20 in tup)
print(tup[0])
print(tup[3])
print(tup[:3]) #slicing
# There is only two built in methods in tuple
print(tup.count(10))
print(tup.index(20))
print(len(tup))

#input in tuple
print()
num = tuple(map(int,input("Enter the tuple: ").split()))
print("the tuple is : ", num)

#operation in tuple
print()
#concat or joining of tuple
tup1 = (1,4,7,9)
tup2 = (2,5,8,10)
tup3 = tup1+tup2
print("the tup3 is: ",tup3)
print(tup1*3)

# country1 = tuple(map(str,input("Enter name of country: ").split()))
# country2 = tuple(map(str,input("Enter name of country: ").split()))
# country3 = country1+country2
# print(country3)

# change in tuple with help of list
num1 = (56,76,96)
temp = list(num1)
temp[1]=66
num1 = tuple(temp)
print("change in tuple: ",num1)

my_list = list(num1)
my_list.append(46)
print("adding element in tuple: ",tuple(my_list))

n = (10,20,30)
my_list1 = list(n)
my_list1.insert(1,15)
print("Insert an element: ", tuple(my_list1))